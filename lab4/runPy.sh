#!/bin/bash

hdfs dfs -rm -r Lab4/output

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="Repartition Join Job via Streaming" \
-files `pwd`/map_combine_files.py,`pwd`/reduce_combine_files.py \
-input Lab4/input/new_auth.txt \
-input Lab4/input/new_hub.txt \
-output Lab4/output/ \
-mapper `pwd`/map_combine_files.py \
-reducer `pwd`/reduce_combine_files.py

hdfs dfs -cat Lab4/output/part-00000