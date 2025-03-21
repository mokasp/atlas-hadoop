#!/bin/bash

# call hdfs dfs to interact with the distributed file system specifically
# and use normal bash commands with the absolute path to make directories
hdfs dfs -mkdir /holbies
hdfs dfs -mkdir /holbies/input