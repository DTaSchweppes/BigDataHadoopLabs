#!/bin/bash

hdfs dfs -mkdir Lab2
hdfs dfs -mkdir Lab2/input

hdfs dfs -put orders.txt Lab2/input/
