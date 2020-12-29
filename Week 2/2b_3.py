import numpy as np

# Write your import_bss function here.

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
  

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)
