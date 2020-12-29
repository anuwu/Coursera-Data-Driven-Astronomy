# Import the running_stats function
from helper import running_stats
from astropy.io import fits
import numpy as np

np.seterr(divide='ignore', invalid='ignore')

# Write your median_bins_fits and median_approx_fits here:

def median_bins_fits (fitslst, B) :
  means, stds = running_stats (fitslst)
  minvals = means - stds
  bwidths = 2*stds/B
  bins = np.zeros (shape = (means.shape[0], means.shape[1], B))
  ignores = np.zeros (shape = means.shape)
  
  for file in fitslst :
    hdulist = fits.open (file)
    data = hdulist[0].data
    
    belmin = data < minvals
    ignores = ignores + belmin.astype(int)
    
    zidx = np.floor((data - minvals)/bwidths).astype (int)
    for i in range (0, B) :
      bins[...,i] += (zidx == i).astype(int)
      
  return (means, stds, ignores, bins)

def median_approx_fits (fitslst, B) :
  means, stds, cumul, bins = median_bins_fits (fitslst, B)
  N = len(fitslst)
  midcnt = (N+1)/2
  
  midbins = (B-1) * np.ones (shape = means.shape)
  for i in range (0, B) :
    cumul += bins[...,i]
    midbins[(cumul >= midcnt) & (midbins == B-1)] = i
    
  minvals = mean - std
  bwidths = 2*stds/B
  medians = minvals + bwidths*(midbins + 0.5)
  
  return medians
  
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with examples from the question.
  
  mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)