# Write your mean_datasets function here

import numpy as np

def mean_datasets (filelist) :
  mean = np.loadtxt (filelist[0], delimiter=',')
  for file in filelist[1:] :
    mean = mean + np.loadtxt (file, delimiter=',')
  
  mean = np.round (mean/len(filelist), 1)
  return mean

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))

