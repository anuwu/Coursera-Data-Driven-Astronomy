# Write your crossmatch function here.
import numpy as np
import time

def angular_dist (cood, cat) :
  return np.degrees(2*np.arcsin(np.sqrt(
    np.square(np.sin((cood[1] - cat[:,1])/2)) +\
    np.cos(cood[1])*np.cos(cat[:,1])*np.square(np.sin((cood[0] - cat[:,0])/2))
  ))).flatten()
  
  
def crossmatch (cat1, cat2, max_dist) :
  t1 = time.perf_counter()
  cat1, cat2 = np.radians(cat1), np.radians(cat2)
  matches, no_matches = [], []
  
  for i, cood in enumerate(cat1) :
    dists = angular_dist(cood, cat2)
    m, d = np.argmin(dists), np.min(dists)
    if d <= max_dist :
      matches.append((i, m, d))
    else :
      no_matches.append(i)
    
  return matches, no_matches, time.perf_counter() - t1



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

