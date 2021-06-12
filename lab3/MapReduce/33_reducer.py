#!/usr/bin/python3
import sys, ast

lastKey = None
H = {}
H[] = []
H1[] = []
for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    key = int(key)
    value = eval(value)
    if len(value) == 3:
  
    if lastKey and lastKey != key:
        for team in H[]:
            for car in H1[]:
                print(str(team[]) + "\t" + str(car))
        H = {}
        H1[] = []
        H[] = []
        if value[] == 'cars':
            H1[].append(value)
        lastKey = key

    else:
        if value[] == 'cars':
            H1[].append(value)
        if value[] == 'teams':
            H[].append(value)
        lastKey = key

if lastKey:
    for team in H[]:
        for car in H1[]:
            print(str(team[]) + "\t" + str(car))
