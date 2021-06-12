#!/usr/bin/env python2.7

import sys

for line in sys.stdin:
    key, values = line.rstrip().split('\t')
    links, weight_hub, weight_auth = values.split(';')
    for link in links[1:-1].split(','):
      if link !='':
        print(link + '\t' + key + '\tlink')
        print(link + '\t' + weight_hub + '\thub')
        #print(key + '\t' + weight_auth + '\tauth')
 
