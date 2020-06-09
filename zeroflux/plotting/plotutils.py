import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogFormatter

def depower(num):
    '''
    Description
      given any number, return value in range 1-10
      as if for scientific notation
      
    Parameters
      num: single value or array
      
    Returns
      removes order of magnitudes,
      resulting in float between 1-10
    '''
    decade = np.floor(np.log10(num)) #order of mag
    return num/(10**(decade))

def minor_log_labels(minor_ticks, axmin, axmax, labmax, skip):
    '''
    Description
      set tick values and labels for log axis 

    Parameters
      minor_ticks: values of axis minor ticks
      axmin: min value of axis
      axmax: max value of axis
      labmax: maximum value in [2,9] to label
      skip: label only every skipth minor axis value
      
    Returns
      minor_ticks: values of new ticks
      minor_labels: new labels adhering to loglabel description 
    '''
    #limit to observable axis range
    minor_ticks = minor_ticks[np.where( (minor_ticks >= axmin) &
                                        (minor_ticks <= axmax) )[0]]
    nticks = len(minor_ticks)
    #set label to '' for depowered tick values > labmax
    minor_depowered = depower(minor_ticks)
    minor_labels = np.array([str(int(val)) for val in minor_depowered])
    minor_labels[minor_depowered > labmax] = ''
    #only show every "skip"th label
    minor_labels[np.arange(nticks) % skip != 0] = ''
    print(minor_labels)
    
    return minor_ticks, minor_labels
    
def loglabel(ax, labmaxx = 7., labmaxy=7., skipx=1, skipy=1, loglabx=True, loglaby=True, useformatter=False):
    '''
    Description
      Sensibly label log10 axes in matplotlib plots
      By default, major labels look like 10^N in latex math mode
      Minor ticks are labeled by single integers, [2,9]
      Use the labmax and skip args to control overcrowding 

    Parameters
      ax: Axes object
      labmaxx: max integer in [2,9] to label on x-axis
      labmaxy: max integer in [2,9] to label on y-axis
      skipx: int, label every nth integer on x-axis
      skipy: int, label every nth integer on y-axis
      loglabx: bool, apply label formatting to x-axis
      loglaby: bool, apply label formatting to y-axis
      useformatter: use ticker.LogFormatter instead
      
    Returns
      ax: Axes object with ticks and labels updated 
    '''
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    
    if useformatter:
        if loglabx:
            Ndecx = np.log10(xmax/xmin)
            ax.xaxis.set_minor_formatter(LogFormatter(labelOnlyBase=False,
                                                      minor_thresholds=(Ndecx*1.2,Ndecx*0.8)))
        if loglaby:
            Ndecy = np.log10(ymax/ymin)
            ax.yaxis.set_minor_formatter(LogFormatter(labelOnlyBase=False,
                                                      minor_thresholds=(Ndecy*1.2,Ndecy*0.8)))
        return ax
    
    else:
        if loglabx:
            minor_xticks = np.array(ax.get_xticks(minor=True))
            new_ticks, new_labels = minor_log_labels(minor_xticks, xmin, xmax, labmaxx, skipx)
            ax.set_xticks(new_ticks, minor=True)
            ax.set_xticklabels(new_labels, minor=True)
        if loglaby:
            minor_yticks = np.array(ax.get_yticks(minor=True))
            new_ticks, new_labels = minor_log_labels(minor_yticks, ymin, ymax, labmaxy, skipy)
            ax.set_yticks(new_ticks, minor=True)
            ax.set_yticklabels(new_labels, minor=True)

        return ax
