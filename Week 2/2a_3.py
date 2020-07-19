# Write your function median_FITS here:

import sys
import numpy as np
from astropy.io import fits
import time

def median_fits (flist) :
  stTime = time.perf_counter ()
  allDat = []
  for file in flist :
    hdulist = fits.open (file)
    data = hdulist[0].data
    allDat.append (data)
  
  allDat = np.asarray (allDat)
  medDat = np.median (allDat, axis=0)
  totTime = time.perf_counter() - stTime

  return (medDat, totTime, allDat.nbytes/1024)
  


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])
