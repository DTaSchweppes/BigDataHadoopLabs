#!/usr/bin/python2.7

import pyhdfs

product_of_interest = raw_input("Name of product: ")
number_of_products_to_show = 10
fs = pyhdfs.HdfsClient(hosts='localhost:50070', user_name='root')
output_file = fs.open('/user/root/lab2/output/part-00000')
top_n_products = {}
for line in output_file:
    line = line.strip().split("\t")
    product_1 = line[0].split(',')[0]
    product_2 = line[0].split(',')[1]
    if product_1 == product_of_interest:
        top_n_products[product_2] = int(line[1])
top_n_products = list(top_n_products.items())
top_n_products.sort(key=lambda x: x[1], reverse=True)
top_n_products = list(top_n_products)[:number_of_products_to_show]
for product in top_n_products:
    print(product)
