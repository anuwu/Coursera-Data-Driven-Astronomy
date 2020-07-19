# Write your mean_fits function here:

import numpy as np
from astropy.io import fits

def mean_fits (fitslist) :
  mean = 0
  for fitsfile in fitslist :
    hdulist = fits.open (fitsfile)
    data = hdulist[0].data
    mean = mean + data
    
  mean = mean/len(fitslist)
  return mean


if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
