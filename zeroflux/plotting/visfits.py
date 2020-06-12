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

def label_angticks(tickvals, tickstride, fmt, axmin, axmax):
    tickvals = tickvals[np.where( (tickvals>=axmin) &
                                  (tickvals<=axmax) )[0]]
    Nticks = int(axmax*tickstride) # number of ticks to reach max
    newticks = np.array([i/tickstride for i in range(Nticks)])
    newlabels = np.array([fmt % i*tickstride for i in np.arange(Nticks)])    
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

    Returns
      ax: Axes object
      im: returned by imshow_norm
    '''
    im, norm = imshow_norm(hdu.data, ax,
                           interval=ZScaleInterval(),
                           stretch=stretch,
                           cmap=cmap)
    if pixscale is not None:
        
        if ticksevery is not None:
            
            #use as many decimal places for label as in ticksevery
            tickstride = ticksevery.to(pixscale.unit).value
            tickstr = str(tickstride)
            if int(tickstride)==tickstride:
                ndec=0
            else:
                ndec = len(tickstr[tickstr.find('.')+1:])
            fmt = "%."+str(ndec)+"f"

            xmin, xmax = ax.get_xlim()
            ymin, ymax = ax.get_ylim()
            newxvals, newxlabs = label_angticks(np.array(ax.get_xticks()),
                                                tickstride, fmt, xmin, xmax)
            newyvals, newylabs = label_angticks(np.array(ax.get_yticks()),
                                                tickstride, fmt, ymin, ymax)
            ax.set_xticks(newxvals)
            ax.set_xlabels(newxlabs)
            ax.set_yticks(newyvals)
            ax.set_ylabels(newylabs)
            unit_str = ' ['+angunit_to_latex(pixscale)+']'
        else:
            unit_str = ' ['+angunit_to_latex(pixscale)+'/pix]'
    else:
        unit_str=''

    
        
    ax.set_xlabel('X coord'+unit_str)
    ax.set_ylabel('Y coord'+unit_str)
    
    return ax, im


