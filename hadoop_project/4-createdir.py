#!/usr/bin/env python2.7
from snakebite.client import Client


def createdir(l):
    client = Client('localhost', 9000)

    for file in l:
        result = client.mkdir([file])
        print(list(result))
