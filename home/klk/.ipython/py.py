# coding=utf-8
import sys
def is2():
	'''
'2.7.13 |Anaconda 4.3.1 (32-bit)| (default, Dec 19 2016, 13:36:02) [MSC v.1500 32 bit (Intel)]
'''
	return sys.version[0]=='2'
def is3():
	'''
'3.5.2 (default, Nov 17 2016, 17:05:23) \n[GCC 5.4.0 20160609]'
'''
	return sys.version[0]=='3'
	
if is2():
	from __builtin__ import *
	
if is3():
	from builtins import *
	
class Class:pass
obj=Class()
instance=type(obj)
classtype=classType=type(Class)