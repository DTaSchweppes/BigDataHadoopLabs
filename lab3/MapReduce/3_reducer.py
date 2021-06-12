#!/usr/bin/python2
import sys, ast

lastKey = None
H = {}
H['A'] = []
H['B'] = []

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    key = int(key)
    value = eval(value)
    
    if lastKey and lastKey != key:
      for a in H['A']:
	for b in H['B']:
	  print (str(b) + "\t" + str(a))
      
      H = {}
      H['A'] = []
      H['B'] = []
      if len(value) == 3:
	H['A'].append(value)
      if len(value) == 2:
	H['B'].append(value)
      lastKey = key
      
    else:
      if len(value) == 3:
	H['A'].append(value)
      if len(value) == 2:
	H['B'].append(value)
      lastKey = key
	 
if lastKey:
    for a in H['A']:
      for b in H['B']:
	print(str(b) + "\t" + str(a))


