#!/usr/bin/env python2.7
""" This file contains a function that utilizes snakebite's Client object to
    connect to and interact with a hadoop distributed file system 
    
    Functions
    ---------
    deletedir(l) : takes in a list of names of directories to delete from
        the Hadoop Distributed File System


    Dependencies
    ------------



    Usage
    -----
    

    
    """
from snakebite.client import Client


def deletedir(l):
    """ function that deletes directories from the Hadoop Distributed File
        system
        
        Args
        ----
        l (list) : list of directory names to remove from HDFS
        
        Returns
        -------
        None

        """
    client = Client('localhost', 9000)
    result = client.delete([l[0]], recurse=True)
    print(list(result))
