#!/usr/bin/env python2.7
""" This file contains a function that utilizes snakebite's Client object to
    connect to and interact with a hadoop distributed file system

    Functions
    ---------
    download(l) : takes in a file name to retrieve from HDFS and copy to the
        local file system


    Dependencies
    ------------
    python 2.7
        - snakebite : python client for interacting with HDFS
    hadoop 3.3.1


    Usage
    -----
    run this command in the terminal:
        python mainfiles/6-main.py

    """
from snakebite.client import Client


def download(l):
    """ function that copies files from the Hadoop Distributed File
        system to the local system's /tmp folder

        Args
        ----
        l (str) : name of file to copy from HDFS to the local fs

        Returns
        -------
        None

        """
    client = Client('localhost', 9000)

    result = client.copyToLocal(l, '/tmp')

    # iterate over generator object to exxecute the action
    for _ in result:
        pass
