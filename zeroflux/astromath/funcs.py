import numpy as np

def rebin2d(arr, new_shape, method='mean'):
    '''
    Code adapted from:
    https://scipython.com/blog/binning-a-2d-array-in-numpy/

    Description
      .Rebins 2D array using mean or sum
      .new shape should consist of factors of old shape

    Parameters
      .arr: 2D numpy array or list
      .new_shape: tuple or list, rows x cols
      .method: string, rebin using 'mean' or 'sum' of values
      
    Returns
      .rebinned 2d numpy array
    '''

    highd_shape = (new_shape[0], np.shape(arr)[0] // new_shape[0],
                   new_shape[1], np.shape(arr)[1] // new_shape[1])

    if method == 'mean':
        return np.reshape(arr, highd_shape).mean(-1).mean(1)
    elif method == 'sum':
        return np.reshape(arr, highd_shape).sum(-1).sum(1)

def sphere_to_cart(rad,theta,phi):
    '''
    Description
      .converts from spherical to cartesian coordinates
      
    Parameters
     .rad: radial coordinate(s)
     .theta: polar angle(s)
     .phi: azimuthal angle(s)

    Returns
     .[x,y,z] array, cartesian coordinates

    '''
    #converts (rad,theta,phi) to (x,y,z)
    #theta->polar, phi->azimuthal 
    x = rad*np.sin(theta)*np.cos(phi)
    y = rad*np.sin(theta)*np.sin(phi)
    z = rad*np.cos(theta)
    return np.array([x,y,z])
    
def cart_to_sphere(x,y,z):
    '''
    Description
      .converts from cartesian to spherical coordinates
      
    Parameters
      .x: x coordinate(s)
      .y: y coordinate(s)
      .z: z coordinate(s)

    Returns
      .[r, theta, phi] array
       theta is polar angle [0,pi]
       phi is azimuthal angle [0,2pi]
    '''
    #converts (x,y,z) to (rad,theta,phi)
    #theta->polar, phi->azimuthal
    rad = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z/r)
    phi = np.arctan(y/x)
    return np.array([rad, theta, phi])


def weighted_mean(x, sig=None, w=None, axis=0):
    '''
    Description
      .calculates weighted arithmetic mean along given axis
      .if weights not provided, uses inverse variance as weights
      
    Parameters
      .x: array values 
      .sig: errors on values, default None
      .w: weights, default None
      .axis: axis to perform averaging over, default 0

    Returns
      .xbar: weighted arithmetic mean of values 
      .sigbar: weighted errors, only if provided
      
    '''
    #normalize weights:
    if weights is None:
        w = 1./sig**2 #inverse variance weights
    w = w/np.sum(w, axis=axis)

    #get weighted average
    xbar = np.sum(x*w, axis=axis)

    #get weighted error
    if sig is not None:
        sigbar = np.sqrt(np.sum(sig**2 * w**2, axis=axis))
        return xbar, sigbar
    
    else:
        return xbar
