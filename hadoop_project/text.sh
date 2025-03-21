#!/bin/bash

# call hdfs to interact with the distributed file system specifically
# and use normal bash commands with the absolute path to output the text of
# a file
hdfs dfs -cat /holbies/input/lao.txt
