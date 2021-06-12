#!/bin/bash

hdfs dfs -mkdir lab2
hdfs dfs -mkdir lab2/input

hdfs dfs -put Order.txt lab2/input/
