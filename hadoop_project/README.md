# Using bash and python to utilize Hadoop's distributed storage and processing utilities

This project explores Hadoop's distributed file system and clustering capabilities

## Set Up and Environment
I am working on a linux environment and i followed [this tutorial](https://www.baeldung.com/linux/hadoop-install-configure). I used ```Hadoop 3.3.1``` and ```Python 2.7``` in a virtual environment. the ```snakebite``` python package is required for some of the tasks aswell.

Be sure to include both ```lao.txt``` and ```salaries.csv``` in your directory.

## Running bash files
Run the first two scripts (Be sure to run ```hdfs dfs -ls -R /``` after each of these to make sure the directories are being created and deleted):

  ```./createdirectories.sh```

  ```./lao.sh```

The third script should print the text from lao.txt:

```./text.sh```



## Running Python - Snakebite files
To run the python scripts that utilize snakebite, you can find run the ```mainfiles``` like so:

```./mainfiles/4-main.py```

```./mainfiles/5-main.py```

```./mainfiles/6-main.py```

Just like with the bash scripts, you can run ```hdfs dfs -ls -R /``` to verify if thw scripts are running properly

## Running mapreduce job
This part can be a little tricky because you must be sure youve specified the file paths correctly, but you are calling files from both your local system and hadoops distributed file system. the command should look like this:

```mapred streaming -input /holbies/input/salaries.csv -output /holbies/output -mapper /<home_folder>/<user>/<project_directory>/<mapper_script.py> -reducer /<home_folder>/<user>/<project_directory>/<reducer_script.py>```

mine looked this for reference:

```mapred streaming -input /holbies/input/salaries.csv -output /holbies/output -mapper /home/hadoop/hadoop_project/mapper.py -reducer /home/hadoop/hadoop_project/reducer.py```

if you mess it up and need to retry, make sure you delete the output directory automatically created when mapred is run by using this command: 

``` hdfs dfs -rm -r /holbies/output```
### Testing mapreduce job without Hadoop
