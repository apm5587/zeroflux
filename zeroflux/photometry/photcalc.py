import numpy as np
from zeroflux.astromath.constants_cgs import c

def SNR_rate(time, source, sky, npix, nsky, dark=0, rn=0):
    '''
    Description
      Calculate SNR given count rates, e/s
      Assumes electrons, not ADU
      
    Parameters
      time: exposure time
      source: count rate of source
      sky: count rate of sky/background
      npix: N pixels used to measure source flux
      nsky: N pixels used to measure background flux
      dark: count rate from dark current
      rn: read noise, gets squared
      
    Returns
      SNR, single value or list of values
    '''
    
    return (source*time) / np.sqrt(source*time + npix*(1+(npix/nsky))*(sky*time+dark*time+rn**2))

def SNR_count(source, sky, npix, nsky, dark=0, rn=0):
    '''
    Description
      Calculate SNR given total counts
      ASsumes electrons, not ADU
      
    Parameters
      source: N counts of source
      sky: N counts of sky/background
      npix: N pixels used to measure source flux
      nsky: N pixels used to measure background flux
      dark: N counts from dark current
      rn: read noise, gets squared
      
    Returns
      SNR, single value or list of values
    '''
    
    return (source) / np.sqrt(source + npix*(1+(npix/nsky))*(sky+dark+rn**2))

def jy_to_mab(fnu):
    '''
    Description
      converts fluxes from Jy to AB magnitudes
      can handle quantity objects

    Parameters
      fnu: single value or list of flux density 
      if no unit given, assumes Jy

    Returns
      single value or list of AB mags
      
    '''
    try:
        fnu.unit
    except AttributeError:
        fnu*=u.Jy
    else:
        fnu = fnu.to(u.Jy)
    
    return -2.5*np.log10(fnu.value) + 8.90

def jy_to_maggie(fnu):
    '''
    Description
      converts fluxes from Jy to maggies
      1 maggie = 3631 Jy
      can handle quantity objects

    Parameters
      fnu: single value or list of flux density 
      if no unit given, assumes Jy

    Returns:
      single value or list of maggies
      
    '''
    
    try:
        fnu.unit
    except AttributeError:
        fnu*=u.Jy
    else:
        fnu = fnu.to(u.Jy)
    
    return fnu.to(u.maggy).

def mab_to_jy(mab):
    '''
    Description
      converts fluxes from AB magnitudes to Jy

    Parameters
      mab: AB mags, single value or list

    Returns
      single value or list of fluxes with Jy units
    '''
    
    return 3631. * 10**(-0.4*mab) *u.Jy

def flam_to_fnu(lam0):
    '''
    Description
      converts from wavelength flux density
      to frequency flux density
      
    Parameters
    
    Returns


    '''
    return

def fnu_to_flam(nu0, freq=True):
    '''
    Description
      converts from frequency flux density
      to wavelength flux density
      
    Parameters
    
    Returns

    '''
    return
