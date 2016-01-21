from os import popen
from re import split

f=popen('dir')
for eachLine in f.readlines():
	print(split(r'\s\s+|\t',eachLine.strip()))
f.close()