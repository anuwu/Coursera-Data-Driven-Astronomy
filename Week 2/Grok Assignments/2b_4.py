import numpy as np

# Write your find_closest function here

def angular_dist(r1, d1, r2, d2) :
  r1, d1, r2, d2 = tuple(np.radians(np.array([r1, d1, r2, d2])))
  return np.degrees(2*np.arcsin(np.sqrt(
    np.square(np.sin((d1 - d2)/2)) +\
    np.cos(d1)*np.cos(d2)*np.square(np.sin((r1 - r2)/2))
  )))

def hms2deg (cood) :
  return 15*(cood[0] + cood[1]/60 + cood[2]/3600)

def dms2deg (cood) :
  return (-1 if cood[0] < 0 else 1)*(np.abs(cood[0]) + cood[1]/60 + cood[2]/3600)

def import_bss() :
  cat = np.loadtxt('bss.dat', usecols=range(1, 7))
  return [
    (i+1, hms2deg(c[0:3]), dms2deg(c[3:6]))
    for i, c in enumerate(cat)
  ]

def find_closest(cat, ra, dec) :
  i, _, _ = min(cat, key=lambda cood : angular_dist(ra, dec, cood[1], cood[2])) 
  return i, angular_dist(ra, dec, cat[i-1][1], cat[i-1][2])

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))

  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))

