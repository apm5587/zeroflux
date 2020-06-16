import numpy as np
import matplotlib.pyplot as plt

from astropy import units as u
from astropy.io import fits
from astropy.visualization import (imshow_norm,
                                   ZScaleInterval,
                                   SquaredStretch,
                                   LinearStretch)

def angunit_to_latex(quantity):
    '''
    Description
      converts astropy angular unit to latex

    Parameters
      quantity: astropy quantity (with unit)

    Returns
      ltx: latex math-mode string 
    '''
    unit_str = str(quantity.unit)
    if unit_str == 'arcsec':
        ltx = r"$^{\prime\prime}$"
    elif unit_str == 'arcmin':
        ltx = r"$^{\prime}$"
    elif unit_str == 'deg':
        ltx = r"$^{\circ}$"
    elif unit_str == 'rad':
        ltx = "rad"

    return ltx

def label_angticks(tickvals, pixscale, tickstride, fmt, axmin, axmax):
    '''
    Description
      calculates new tick positions and labels
      for angular units

    Parameters
      tickvals: result of ax.get_xticks() (or y)
      pixscale: pixel scale with unit
      tickstride: number of pixels between ticks
      fmt: how to format string labels
      axmin: from ax.get_xlim() (or y)
      axmax: from ax.get_xlim() (or y)
      
    Returns
      newticks: new tick positions in units of pixels
      newlabels: the labels in terms of angular units for newticks
    '''
    tickvals = tickvals[np.where( (tickvals>=axmin) &
                                  (tickvals<=axmax) )[0]] #restrict to observable axis 
    Nticks = int(axmax/tickstride)+1 # number of ticks to reach max
    print(Nticks)
    newticks = np.array([i*tickstride for i in range(Nticks)]) #tick positions, pixels
    labvals = np.array([tick*pixscale.value for tick in newticks]) #tick labels, angular units
    newlabels = np.array([fmt % (val) for val in labvals]) #format decimal places
     
    return newticks, newlabels

def showds9(ax, hdu, stretch=LinearStretch(), cmap='gray',
            pixscale=None, ticksevery=None):
    '''
    Description
      Uses astropy.visualization's imshow_norm
      to mimic viewing fits images with
      zscale in DS9
      
    Parameters
      ax: Axes object
      hdu: fits HDU object with data
      stretch: see astropy.visualization for options
      cmap: matplotlib color map
      pixscale: pixel scale WITH astropy unit attached
      tickevery: label tick marks every __ angular units
                 requires pixscale
                 the axis unit will adopt this unit

    Returns
      ax: Axes object
      im: returned by imshow_norm
    '''
    im, norm = imshow_norm(hdu.data, ax, origin='lower',
                           interval=ZScaleInterval(),
                           stretch=stretch,
                           cmap=cmap)
    if pixscale is not None:
        scaleunit = pixscale.unit
        
        if ticksevery is not None:
            #convert pixscale to ticksevery unit
            ticksunit = ticksevery.unit
            pixscale = pixscale.to(ticksunit)
            #N pixels per tick label
            tickstride = (ticksevery/pixscale).value 
            tickstr = str(ticksevery.value)
            #use as many decimal places for label as in ticksevery
            if int(ticksevery.value)==ticksevery.value:
                ndec=0
            else:
                ndec = len(tickstr[tickstr.find('.')+1:])
            fmt = "%."+str(ndec)+"f"

            #get axes limits in units of pixels
            xmin, xmax = ax.get_xlim()
            ymin, ymax = ax.get_ylim()
            print('xlim', xmin, xmax)
            print('ylim', ymin, ymax)
            print('yvals', ax.get_yticks())
            
            #re-label x
            newxvals, newxlabs = label_angticks(np.array(ax.get_xticks()),
                                                pixscale, tickstride, fmt, xmin, xmax)
            #re-label y
            newyvals, newylabs = label_angticks(np.array(ax.get_yticks()),
                                                pixscale, tickstride, fmt, ymin, ymax)
            print(newyvals)
            print(newylabs)
            ax.set_xticks(newxvals)
            ax.set_xticklabels(newxlabs)
            ax.set_yticks(newyvals)
            ax.set_yticklabels(newylabs)
            unit_str = ' ['+angunit_to_latex(pixscale)+']'
        else:
            unit_str = ' ['+str(pixscale.value)+angunit_to_latex(pixscale)+'/pix]'
    else:
        unit_str='pix'

    #label units
    ax.set_xlabel('X'+unit_str)
    ax.set_ylabel('Y'+unit_str)
    
    return ax, im
