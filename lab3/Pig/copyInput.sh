#!/bin/bash

hdfs dfs -rm -r laba3
hdfs dfs -mkdir laba3
hdfs dfs -mkdir laba3/input

hdfs dfs -put data_teams.txt laba3/input/
hdfs dfs -put data_cars.txt laba3/input/
hdfs dfs -put data_teammembers.txt laba3/input/
hdfs dfs -put script.pig laba3/input/
