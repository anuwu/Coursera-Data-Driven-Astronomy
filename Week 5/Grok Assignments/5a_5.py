import numpy as np

# Write your query function here
def query(star_csv, planet_csv) :
  stars = np.loadtxt(star_csv, usecols=[0, 2], delimiter=',') 
  planets = np.loadtxt(planet_csv, usecols=[0, 5], delimiter=',')
  
  ret = []
  for p in planets :
    s = stars[:,0] == p[0]
    if s.any() :
      s = stars[s].flatten()
      if s[1] > 1 :
        ret.append(p[1]/s[1])

  return np.sort(np.array(ret)).reshape(-1,1)
  

# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv', 'planets.csv')
  print(result)
