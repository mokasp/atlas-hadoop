#!/bin/bash
# call hdfs to interact with the distributed file system specifically
# and use normal bash commands with the absolute path to put a local file
# into the hadoop file system
hdfs dfs -put lao.txt /holbies/input