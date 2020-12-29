# Write your median_bins and median_approx functions here.

import numpy as np

def median_bins (lst, B) :
  lst = np.asarray (lst)
  mu = np.mean (lst)
  sigma = np.std (lst)
  minval = mu - sigma
  maxval = mu + sigma
  bwidth = 2*sigma/B
  
  ignore = 0
  counts = np.zeros (B)
  for i in range(0, lst.size) :
    if lst[i] < minval :
      ignore = ignore + 1
    elif lst[i] < maxval :
      j = int(np.floor ((lst[i] - minval)/bwidth))
      counts[j] = counts[j] + 1
  
  return (mu, sigma, ignore, counts)

def median_approx (lst, B) :
  midcnt = (len(lst) + 1) / 2
  mu, sigma, ignore, counts = median_bins (lst, B) 
  bwidth = 2*sigma/B
  minval = mu - sigma
  
  tot = ignore
  i = 0
  while i < counts.size :
    tot = tot + counts[i]
    if tot >= midcnt :
      break
    i = i + 1
    
  if i == counts.size :
    i -= 1
  return minval + bwidth*(i + 0.5)
    
  
  

# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
  
  print(median_bins([1, 1, 1000], 5))
  print(median_approx([1, 1, 1000], 5))

