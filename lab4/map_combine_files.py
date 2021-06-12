#!/usr/bin/env python2.7
import os
import sys

for line in sys.stdin:
    key, value = line.rstrip().split(';') 
    file_name = os.environ['mapreduce_map_input_file']
    if 'new_auth' in file_name:
      print(key+';hub;'+value)
    elif 'new_hub' in file_name:
      print(key+';auth;'+value)