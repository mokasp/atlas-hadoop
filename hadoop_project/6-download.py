#!/usr/bin/env python2.7
from snakebite.client import Client


def download(l):
    client = Client('localhost', 9000)

    result = client.copyToLocal(l, '/tmp')

    # iterate over generator object to exxecute the action
    for _ in result:
        pass
