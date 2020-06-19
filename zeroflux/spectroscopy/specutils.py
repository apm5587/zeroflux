import numpy as np

class Spectrum:
    '''
    Basic functionality for working with 1D spectrum
    '''
    
    def __init__(self, wav, flux, err=None, zred=0.0, frame='obs'):

        #input properties
        self.wav = np.array(wav)
        self.flux = np.array(flux)
        self.err = np.array(err)
        self.zred = zred
        self.frame = frame

        #derived properties
        self.wavdiff = np.diff(wav)
        if np.all(self.wavdiff[0]==self.wavdiff):
            self.dwav = self.wavdiff[0] #dwav wav units per bin 
        else:
            print('warning, non-rectified wavelength scale...')
        

    def redshift(self, z=None):
        if z is None
            z = self.zred

        #shift wavelengths, update frame
        if self.frame == 'obs':
            self.wav /= (1.+z)
            self.frame = 'rest'
            
        elif self.frame == 'rest':
            self.wav *= (1.+z)
            self.frame='obs'

    def fitline_opt():
        return
    
    def fitline_mcmc():
        return
    
    def linesearch():
        return
        
        

        
        
