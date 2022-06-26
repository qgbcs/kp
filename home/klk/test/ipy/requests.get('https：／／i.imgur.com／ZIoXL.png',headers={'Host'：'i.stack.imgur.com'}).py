#coding=utf-8
import sys;'qgb.U' in sys.modules or sys.path.append('/home/klk/');from qgb import *
ws=F.dl(F.ls(U.gst)[-1])                                                # 1 
#from qgb import *                                                      # 2 
ws=F.dl(F.ls(U.gst)[-1])                                                # 3 
_4=U.searchIterable(ws,'twitt')                                         # 4 
_5=U.searchIterable(ws,'img')                                           # 5 
_6=U.searchIterable(ws,'imgu')                                          # 6 
#get_ipython().system('curl -vvi')                                      # 7 
#get_ipython().system('curl -vvi https://i.stack.imgur.com/ZIoXL.png')  # 8 
#get_ipython().system('curl -vvi https://i.imgur.com/ZIoXL.png')        # 9 
#get_ipython().system('curl -vvi https://i.stack.imgur.com/ZIoXL.png')  # 10 
#get_ipython().system('dig i.stack.imgur.com')                          # 11 
import requests                                                         # 12 
_13=requests.get('https://i.imgur.com/ZIoXL.png',headers={'Host':'i.stack.imgur.com'})  # 13 
_14=len(_13.content)                                                    # 14 
#_15=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 15 
_16=N.rpc_set(_13.content)                                              # 16 
_17=requests.get('https://i.imgur.com/ZIoXL.png',headers={'Host':'i.stack.imgur.com'})  # 17 
#ipy.save(_i)                                                           # 18 
