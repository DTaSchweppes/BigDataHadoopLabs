#!/usr/bin/env python2.7
# Advisor.py
from ast import literal_eval

import pyhdfs

product_of_interest = raw_input("Name of product: ")
number_of_products_to_show = 10
fs = pyhdfs.HdfsClient(hosts='localhost:50070', user_name='root')
output_file = fs.open('/user/root/Lab2/output/part-00000')
top_n_products = {}

for line in output_file:
    line = line.strip().split("\t")
    product = line[0]
    dict_ = literal_eval(line[1])
    if product == product_of_interest:
        associative_array = sorted(dict_.items(), key=lambda item: item[1], reverse=True)
        print(product_of_interest, dict(associative_array[:10]))
