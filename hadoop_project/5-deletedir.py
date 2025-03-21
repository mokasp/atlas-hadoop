#!/usr/bin/env python2.7
from snakebite.client import Client


def deletedir(l):
    client = Client('localhost', 9000)
    result = client.delete([l[0]], recurse=True)
    print(list(result))
