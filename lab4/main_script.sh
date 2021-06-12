#!/bin/bash

#sh ./copyInput.sh
#sh ./runPy.sh

hdfs dfs -rm -r HITS
# copy initial files
hdfs dfs -mkdir HITS
hdfs dfs -mkdir HITS/itr_1
hdfs dfs -put input.txt HITS/itr_1

#
itr_count=2
for ((itr=1; itr <= $itr_count; itr++)); do
    echo "Doing iteration $itr of $itr_count..."
    #hdfs dfs -rm -r HITS/itr_$((itr+1))
    hdfs dfs -rm -r HITS/new_auth
    hdfs dfs -rm -r HITS/new_hub
    hdfs dfs -rm -r HITS/new_hub_stage_1
    #####################################################################
    # Calculating new hub points
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -D mapreduce.job.name="Calculating new auth points" \
        -files $(pwd)/map_auth.py,$(pwd)/reduce_auth.py \
        -input HITS/itr_$itr/ \
        -output HITS/new_auth/ \
        -mapper $(pwd)/map_auth.py \
        -reducer $(pwd)/reduce_auth.py
    #####################################################################
    # Calculating new auth points 
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -D mapreduce.job.name="Calculating new hub points (stage 1 of 2)" \
        -files $(pwd)/map_hub_1.py,$(pwd)/reduce_hub_1.py \
        -input HITS/itr_$itr/ \
        -output HITS/new_hub_stage_1/ \
        -mapper $(pwd)/map_hub_1.py \
        -reducer $(pwd)/reduce_hub_1.py
        
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -D mapreduce.job.name="Calculating new hub points (stage 2 of 2)" \
        -files $(pwd)/map_hub_2.py,$(pwd)/reduce_hub_2.py \
        -input HITS/new_hub_stage_1/ \
        -output HITS/new_hub/ \
        -mapper $(pwd)/map_hub_2.py \
        -reducer $(pwd)/reduce_hub_2.py
    #####################################################################
    # Merging calculated points into one file
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -D mapreduce.job.name="Final step of calculation" \
        -files $(pwd)/map_combine_files.py,$(pwd)/reduce_combine_files.py \
        -input HITS/new_auth/ \
        -input HITS/new_hub/ \
        -output HITS/itr_$((itr+1))/ \
        -mapper $(pwd)/map_combine_files.py \
        -reducer $(pwd)/reduce_combine_files.py

done
hdfs dfs -cat HITS/itr_$((itr_count+1))/*