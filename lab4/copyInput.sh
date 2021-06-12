#!/bin/bash

hdfs dfs -rm -r Lab4
hdfs dfs -mkdir -p Lab4/input

hdfs dfs -put new_hub.txt Lab4/input
hdfs dfs -put new_auth.txt Lab4/input
