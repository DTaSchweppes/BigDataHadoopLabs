#!/bin/bash

hdfs dfs -rm -r Lab2.1/output

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="Cross Job via Streaming" \
-files `pwd`/1.py,`pwd`/2.py,`pwd`/Format.py \
-input Lab2.1/input/ \
-output Lab2.1/output/ \
-mapper `pwd`/1.py \
-combiner `pwd`/2.py \
-reducer `pwd`/2.py

hdfs dfs -cat Lab2.1/output/part-00000

python Format.py
