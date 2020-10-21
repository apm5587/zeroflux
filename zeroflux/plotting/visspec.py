import numpy as np
import matplotlib.pyplot as plt

def plotspec(ax, wav, flux, err=None, show_err=True,
             window_center=None, window_size=None,
             xunit=r'$[\mathrm{\AA}]$',
             yunit=r'$[\mathrm{erg \ s^{-1} \ cm^{-2} \ {\AA}^{-1}}]$',
             **kwargs):
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
      xunit: string describing x-axis unit
      yunit: string describing y-axis unit

    Returns
      Axes object
    '''
    
    #only look at wavelength window, if provided
    if window_center is not None and window_size is not None:
        #index of window center
        center_idx = np.argmin(np.abs(wav-window_center))
        window = np.arange(center_idx-window_size,
                           center_idx+window_size)
        wav = wav[window]
        flux = flux[window]
        errs = errs[window]

    #step plot for fluxes
    ax.step(wav, flux, where='mid', **kwargs)

    #add errorbars 
    if show_err:
        ax.errorbar(wav, flux, yerr=err, 
                    fmt='none', **kwargs)

    #label with customizable units
    ax.set_xlabel('Wavelength ' + xunit)
    ax.set_ylabel('Flux ' + yunit)
    
    return ax
