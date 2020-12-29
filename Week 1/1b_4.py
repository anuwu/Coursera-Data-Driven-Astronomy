# Write your load_fits function here.

import numpy as np
from astropy.io import fits

def load_fits (filename) :
  hdulist = fits.open (filename)
  data = hdulist[0].data
  ind = np.unravel_index(np.argmax(data, axis=None), data.shape)
  return ind


if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

 

