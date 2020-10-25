import numpy as np

# Write your angular_dist function here.

def angular_dist(r1, d1, r2, d2) :
  r1, d1, r2, d2 = tuple(np.radians(np.array([r1, d1, r2, d2])))
  return np.degrees(2*np.arcsin(np.sqrt(
    np.square(np.sin((d1 - d2)/2)) +\
    np.cos(d1)*np.cos(d2)*np.square(np.sin((r1 - r2)/2))
  )))

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  # Run your function with the second example in the question
  print(angular_dist(10.3, -3, 24.3, -29))

