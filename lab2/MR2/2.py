#!/usr/bin/env python2.7

import sys
from ast import literal_eval
from collections import Counter

(lastkey, appl_dict) = (None, {})

for line in sys.stdin:
    (key, mass) = line.strip().split("\t")
    mass = literal_eval(mass)
    if lastkey and lastkey != key:
        print(lastkey + '\t' + str(appl_dict))
        (lastkey, appl_dict) = (key, mass)
    else:
        lastkey = key
        appl_dict = dict(Counter(appl_dict) + Counter(mass))
if lastkey:
    print(lastkey + '\t' + str(appl_dict))