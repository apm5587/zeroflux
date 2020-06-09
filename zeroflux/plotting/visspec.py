import numpy as np
import matplotlib.pyplot as plt

def plotspec(ax, wav, flux, err=None, show_err=True,
             window_center=None, window_size=None,
             dcolor='b', ecolor='k',
             xunit=r'$[\mathrm{\AA}]$'
             yunit=r'$[\mathrm{erg \ s^{-1} \ cm^{-2} \ {2\AA}^{-1}}]$'
    '''
    Description
      Plot 1D spectrum with errorbars
      can provide a viewing window to see specific wavelength range

    Parameters
      ax: Axes object
      wav: wavelength values
      flux: flux/count values
      err: error values
      show_err: bool, plot errorbars
      window_center: window center in units of wav
      window_size: window size (+/- ws) in terms of indices 
      dcolor: color for data
      ecolor: color for error bars
      xunit: string for units of x-axis
      yunit: string for units of y-axis

    Returns
      Axes object
    '''
    
    #only look at wavelength window if provided
    if wc is not None and ws is not None:
        #index of window center
        center_idx = np.argmin(np.abs(wav-wc))
        window = np.arange(center_idx-ws, center_idx+ws)
        wav = wav[window]
        cnts = cnts[window]
        errs = errs[window]

    #step plot for fluxes
    ax.step(wav, cnts, where='mid', color=dcolor)

    #add errorbars 
    if show_err:
        ax.errorbar(wav, cnts, yerr=err, 
                    fmt='none', color=ecolor, alpha=0.5)
        
    ax.set_xlabel('Wavelength ' + xunit)
    ax.set_ylabel('Flux ' + yunit)
    
    return ax
