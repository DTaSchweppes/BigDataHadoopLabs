#!/usr/bin/env python2.7

import sys

last_key, links, weight_hub, weight_auth = None, [], 0, 0
for line in sys.stdin:
    key, label, values = line.rstrip().split(';')
    if last_key and last_key != key:
        print(str(last_key) + ';'  + str(weight_hub) + ';' + str(weight_auth))
        weight_hub = 0
        weight_auth = 0
        links = []
    if label == 'hub':
        weight_hub += int(values)
    elif label == 'auth':
        weight_auth += int(values)
    elif label == 'link':
        links.append(values)
    last_key = key

if last_key:
    print(str(last_key) + ';' + str(weight_hub) + ';' + str(weight_auth))
        