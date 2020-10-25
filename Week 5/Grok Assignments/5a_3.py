import numpy as np

# Write your query function here
def query (file) :
  dat = np.loadtxt(file, usecols=[0,2], delimiter=',')
  return dat[dat[:,1] > 1] 

# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
  print(result)
