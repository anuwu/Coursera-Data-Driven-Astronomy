import numpy as np

# Write your crossmatch function here.

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

def import_super() :
  cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  return [
    (i+1, c[0], c[1])
    for i, c in enumerate(cat)
  ]

def angular_dist(r1, d1, r2, d2) :
  r1, d1, r2, d2 = tuple(np.radians(np.array([r1, d1, r2, d2])))
  return np.degrees(2*np.arcsin(np.sqrt(
    np.square(np.sin((d1 - d2)/2)) +\
    np.cos(d1)*np.cos(d2)*np.square(np.sin((r1 - r2)/2))
  )))

def find_closest(cat, ra, dec) :
  i, _, _ = min(cat, key=lambda cood : angular_dist(ra, dec, cood[1], cood[2])) 
  return i, angular_dist(ra, dec, cat[i-1][1], cat[i-1][2])

def crossmatch (cat1, cat2, max_dist) :
  matches, no_matches = [], []
  for obj in cat1 :
    i, dist = find_closest(cat2, obj[1], obj[2])
    if dist <= max_dist :
      matches.append((obj[0], i, dist))
    else :
      no_matches.append(obj[0])
  return matches, no_matches


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

