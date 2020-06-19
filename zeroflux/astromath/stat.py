import numpy as np
from numpy import pi

def sample_sphere_phi(unif):
    '''
    Description
      .Sample azimuthal angle uniformly over sphere
      .phi in [0,2pi]

    Parameters:
      .unif: uniform random variable(s), [0,1]

    Returns:
      .phi value(s) sampled over sphere 
    '''
    return 2*pi*unif

def sample_sphere_theta(unif):
    '''
    Description
      .Sample polar angle uniformly over sphere
      .theta in [0,pi]

    Parameters:
      .unif: uniform random variable(s), [0,1]

    Returns:
      .theta value(s) sampled over sphere 
    '''
    '''
    #returns uniform theta (polar angle) distribution, [0,pi]
    ''' 
    return np.arccos(1. - 2.*unif)
