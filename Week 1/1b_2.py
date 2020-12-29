# Write your calc_stats function here.

import numpy as np

def calc_stats (filename) :
  data = np.loadtxt (filename, delimiter=',')
  data = np.sort (data.flatten())
  sz = np.size (data)
  if sz % 2 :
    med = data[int(sz/2)]
  else :
    med = (data[int(sz/2)] + data[int(sz/2) - 1]) / 2
    
  med = round (med, 1)
  mean = round (np.mean(data), 1)
  return (mean, med)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data2.csv')
  print(mean)
