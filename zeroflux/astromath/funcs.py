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


