import numpy as np
import matplotlib.pyplot as plt

from astropy.io import fits
from astropy.visualization import (imshow_norm,
                                   ZScaleInterval,
                                   SquaredStretch,
                                   LinearStretch)

def showds9(ax, hdu, stretch=LinearStretch(), cmap='gray'):
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

    Returns
      ax: Axes object
      im: returned by imshow_norm
    '''
    im, norm = imshow_norm(hdu.data, ax,
                           interval=ZScaleInterval(),
                           stretch=stretch,
                           cmap=cmap)
    ax.set_xlabel('X coord')
    ax.set_ylabel('Y coord')
    return ax, im


