import numpy as np
from astropy.wcs import WCS

try:
    from reproject import reproject_interp
except ModuleNotFoundError
    print('Warning: reproject package not installed')

def calibrate_sci(sci, flt, zro, exptime=True):
    '''
    Description
      subtracts bias and flat fields science image
      
    Parameters
      sci: science hdu
      flt: master flat hdu
      zro: master bias hdu
      exptime: bool, divide sci by exposure time
      
    Returns
      None
    '''
    
    bias_sub = sci.data-zro.data
    flat_fielded = bias_sub/flt.data
    if exptime:
        #divide by exposure time
        flat_fielded /= sci.header['EXPTIME']
    sci.data = flat_fielded
                  
    return


def reproj(base, rep):
    '''
    Description
      reproject one image onto another, update wcs
      uses interpolation from reproject package
      
    Parameters
      base: hdu of image to project on to
      rep: hdu of image to be reprojected
      
    Returns
      None
    '''

    #get wcs of base image
    wcs_b = WCS(base.header)
    #perform reprojection
    array, footprint = reproject_interp(rep, base.header)
    #replace rep data with reprojected data
    rep.data = array
    #update rep header to include base wcs
    rep.header.update(wcs_b.to_header()) 
    
    return

def make_master_flat(hdus, mzro):
    '''
    Description
      uses median of flats to make master flat data
      
    Parameters
      hdus: list of hdus for flats
      mzro: master bias data
      
    Returns
      master flat data array
    '''
    #subtract master bias individually
    data = np.array([hdu.data-mzro for hdu in hdus])
    #convert to counts/s
    data = np.array([dat/float(hdu.header['EXPTIME']) for dat,hdu in zip(data, hdus)])
    #take median of each pixel 
    med_flt =  np.median(data, axis=0)
    #return normalized master flat
    return med_flt/np.mean(med_flt)

def make_master_bias(hdus):
    '''
    Description
      uses median of bias frames to make master bias data
      
    Parameters
      hdus: list of hdus for bias frames
      
    Returns
      master bias data array
    '''
    
    data = np.array([hdu.data for hdu in hdus])
    #return median in each pixel
    return np.median(data, axis=0) 
