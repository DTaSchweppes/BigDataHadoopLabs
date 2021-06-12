#!/usr/bin/env python2.7

import sys

for line in sys.stdin:
  line = line.strip().split(" ")
  for i in range(len(line)):
    for j in range(i+1, len(line)):
      if line[i] < line[j]:
	print(line[i] + ',' + line[j] + '\t1')
      else:
	print(line[j] + ',' + line[i] + '\t1')