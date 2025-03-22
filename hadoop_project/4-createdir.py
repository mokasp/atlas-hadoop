#!/usr/bin/env python2.7
""" This file contains a function that utilizes snakebite's Client object to
    connect to and interact with a hadoop distributed file system 
    
    Functions
    ---------
    createdir(l) : takes in a list of names of directories to create and
        creates them on the Hadoop Distributed File System


    Dependencies
    ------------
    python 2.7
        - snakebite : python client for interacting with HDFS
    hadoop 3.3.1


    Usage
    -----
    

    
    """
from snakebite.client import Client


def createdir(l):
    """ function that creates directories on the Hadoop Distributed File
        system
        
        Args
        ----
        l (list) : list of directory names to create on HDFS
        
        Returns
        -------
        None
        
        """
    client = Client('localhost', 9000)

    for file in l:
        result = client.mkdir([file])
        print(list(result))
