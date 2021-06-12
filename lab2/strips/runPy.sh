#!/bin/bash

hdfs dfs -rm -r Lab2/output

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="Cross Job via Streaming" \
-files `pwd`/1.py,`pwd`/2.py,`pwd`/Format.py \
-input Lab2/input/ \
-output Lab2/output/ \
-mapper `pwd`/1.py \
-combiner `pwd`/2.py \
-reducer `pwd`/2.py

hdfs dfs -cat Lab2/output/part-00000

python Format.py
