#! /usr/bin/env python3.3
import re
import argparse

#Now we parse arg

thearg = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
thearg.add_argument("file", type=list, help="the file to be proceed")

#

#Open file
f = open('workfile', 'r')
