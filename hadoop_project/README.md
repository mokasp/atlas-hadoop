# Using bash and python to utilize Hadoop's distributed storage and processing utilities

This project explores Hadoop's distributed file system and clustering capabilities

## Set Up and Environment
I am working on a linux environment and i followed [this tutorial](https://www.baeldung.com/linux/hadoop-install-configure). I used the ```Hadoop 3.3.1``` and ```Python 2.7``` in a virtual environment. the ```snakebite``` package is required for some of the tasks aswell.

Be sure to include both ```lao.txt``` and ```salaries.csv``` in your directory.

## Running bash files
Run the first two scripts (Be sure to run ```hdfs dfs -ls -R /``` after each of these to make sure the directories are being created and deleted):

  ```./createdirectories.sh```

  ```./lao.sh```

The third script should print the text from lao.txt:

```./text.sh```



## Running Python - Snakebite files

## Running mapreduce job

### Testing mapreduce job without Hadoop
