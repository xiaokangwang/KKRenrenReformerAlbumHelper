#! /usr/bin/env python3.3
import re
import argparse

def reimageline(stringtoparse):
	pass

#show brief use of this script

print("KKRenrenReformer --- a script help user to parse saved album by Renren Reformer")

#Now we parse arg

thearg = argparse.ArgumentParser()
group = thearg.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
thearg.add_argument("file", help="the file to be proceed")
args = thearg.parse_args()

#make args into data to be used later

filename=args.file

#Open file

f = open(filename, 'r')
htmldata=f.read()
lines=reimageline(htmldata)



