import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
  meantime = 0
  for i in range (0, ntrials) :
    data = np.random.rand(size)
    
    start = time.perf_counter()
    res = func(data)
    tm = time.perf_counter() - start
    
    meantime = meantime + tm
    
    
  return meantime/ntrials

if __name__ == '__main__':
  print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
  print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))
