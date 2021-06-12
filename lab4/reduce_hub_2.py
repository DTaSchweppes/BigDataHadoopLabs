#!/usr/bin/env python2.7

import sys

last_key, links, weight_hub = None, [], 0
for line in sys.stdin:
    key, values, label = line.rstrip().split('\t')
    if last_key and last_key != key:
	links.sort()
        print(str(last_key) + '\t' + '(' + ",".join(links) + ');' + str(weight_hub))
        weight_hub = 0
        links = []
    if label == 'hub':
        weight_hub += int(values)
    elif label == 'link':
        links.append(values)
    last_key = key

if last_key:
    links.sort()
    print(str(last_key) + '\t' + '(' + ",".join(links) + ');' + str(weight_hub))
        