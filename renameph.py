#! /usr/bin/env python3.3
import re
import argparse
from shutil import copy

def reimageline(stringtoparse):

	re_imageli = re.compile("""<img height="128" width="128" index="\d*" src="[^ \t\n\r\f\v]*" title="[^\t\n\r\f\v]*?">""")

	thelist = re_imageli.findall(stringtoparse)

	return thelist
	pass

def getinfo(stringtoparse):
	imginfo={}

	re_imgind = re.compile(""" index="(\d+)" """)
	re_imgsrc = re.compile(""" src="([^\t\n\r\f\v]+?)" """)
	re_imgtitle = re.compile(""" title="([^\t\n\r\f\v]+)">""")

	imginds = re_imgind.findall(stringtoparse)
	imginfo["ind"]=imginds[0]

	imgsrc = re_imgsrc.findall(stringtoparse)
	imginfo["src"]=imgsrc[0]

	showifv("image {0} was parsed into info.It's location {1} was known.".format(imginds[0],imgsrc[0]))

	#not used and cause bug
	#imgtitle = re_imgtitle.findall(stringtoparse)
	#imginfo["tit"]=imgtitle[0]

	return imginfo

def createnewfilename(itemtoproceed):
	#get html nane without ext

	re_htmlname = re.compile("""^([^\t\n\r\f\v]+?)\.(html|htm)$""")
	htmlname = re_htmlname.findall(filename) 
	thehtmlname = htmlname[0][0]

	#get image file ext
	theimgext = itemtoproceed["src"][-3:]

	#create new name

	the_filename_new=thehtmlname+"-"+itemtoproceed['ind'].zfill(3)+"."+theimgext
	itemtoproceed["new_name"]=the_filename_new

def imgname_apply_change(applyitem):
	copy(applyitem['src'],"./KKRenrenReformerImage/"+applyitem['new_name'])
	showifv("image {0} was copyed into new location, with it's new name {1} .".format(applyitem['ind'],applyitem['new_name']))
	pass

def showifv(message):
	if(is_verbose):
		print(message)
	pass

def shownq(message):
	if(is_quiet!=True):
		print(message)
	pass

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
is_verbose=args.verbose
is_quiet=args.quiet

#Open file

f = open(filename, 'r')
showifv("html file {0} was opened.".format(filename))

#read file

htmldata=f.read()
showifv("The content of html file {0} was loaded.".format(filename))

#progress the html file

lines=reimageline(htmldata)
showifv("We have parsed html file {0} ,and {1} record was come into known.".format(filename,len(lines)))

img_info=[]

for line_element in lines:
	alineinfo=getinfo(line_element)
	img_info.append(alineinfo)
showifv("information of {0} image was known.".format(len(img_info)))

#Create new filename
for img_info_element in img_info:
	createnewfilename(img_info_element)
showifv("New name of {0} image was create.".format(len(img_info)))

#apply new file name
filecount=0
for img_info_element in img_info:
	imgname_apply_change(img_info_element)
	filecount=filecount + 1
showifv("New name of {0} image was applyed.".format(len(img_info)))


shownq("Done! {0} was proceed and {1} files was copyed.".format(filename,filecount))




