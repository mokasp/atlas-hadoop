#!/usr/bin/env python2.7
from snakebite.client  import Client


def createdir(l):
    client = Client('localhost', 9000)
    print('hi')

    for file in l:
        result = client.mkdir([file])
        print(list(result))
    
    # result = client.delete([l[0]], recurse=True)
    # print(list(result))
