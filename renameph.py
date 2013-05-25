#! /usr/bin/env python3.3
import re
import argparse

def reimageline(stringtoparse):
	re_imageli = re.compile("""<img height="128" width="128" index="\d*" src="[^ \t\n\r\f\v]*" title="[^\t\n\r\f\v]*?">""")
	thelist = re_imageli.findall(stringtoparse)
	return thelist
	pass

def getinfo(stringtoparse):
	imginfo={}
	re_imgind = re.compile(""" index="(\d+)" """)
	re_imgsrc = re.compile(""" src="([^\t\n\r\f\v]+)" """)
	re_imgtitle = re.compile(""" title="([^\t\n\r\f\v]+)">""")
	imginds = re_imgind.findall(stringtoparse)
	imginfo["ind"]=imginds[0]
	imgsrc = re_imgsrc.findall(stringtoparse)
	imginfo["src"]=imgsrc[0]
	imgtitle = re_imgtitle.findall(stringtoparse)
	imginfo["tit"]=imgtitle[0]
	return imginfo


#show brief use of this script

print("KKRenrenReformer --- a script help user to parse saved album by Renren Reformer")

#Now we parse arg

thearg = argparse.ArgumentParser()
group = thearg.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true",help="Out put as much as possible, useful in debuging")
group.add_argument("-q", "--quiet", action="store_true",help="No any out put")
thearg.add_argument("file", help="the file to be proceed")
args = thearg.parse_args()

#make args into data to be used later

filename=args.file

#Open file

f = open(filename, 'r')

#read file

htmldata=f.read()

#progress the file

lines=reimageline(htmldata)
img_info=[]
for line_element in lines:
	alineinfo=getinfo(line_element)
	img_info.append(alineinfo)
print(img_info)



