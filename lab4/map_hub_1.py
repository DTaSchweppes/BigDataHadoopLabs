#!/usr/bin/env python2.7

import sys

for line in sys.stdin:
    key, values = line.rstrip().split('\t')
    links, weight_hub, weight_auth = values.split(';')
    print(key + '\t' + weight_hub + '\thub')
    for link in links[1:-1].split(','):
        print(link + '\t' + key + '\tlink')
