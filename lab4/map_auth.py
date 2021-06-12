#!/usr/bin/env python2.7

import sys

for line in sys.stdin:
    key, values = line.rstrip().split('\t')
    links, weight_auth, weight_hub = values.split(';')
    links = tuple(links[1:-1].split(","))
    for link in links:
        print(key + '\t' + link + '\tlink')
        print(link + '\t' + weight_hub + '\thub')