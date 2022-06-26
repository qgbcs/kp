#coding=utf-8
import sys;'qgb.U' in sys.modules or sys.path.append('/home/klk/');from qgb import *
#from qgb import *                                                      # 1 
#get_ipython().magic('ls ')                                             # 2 
#_3=U.cdt()                                                             # 3 
#get_ipython().magic('ls ')                                             # 4 
#get_ipython().magic('cd github.com/')                                  # 5 
#get_ipython().magic('ls ')                                             # 6 
#_7=F.ls()                                                              # 7 
#_8=F.dl(_[0])                                                          # 8 
#F.dl(U.pwd+F.ls()[0])                                                  # 9 
#F.dl( U.pwd+F.ls()[0])                                                 # 10 
#_11=F.dl( U.pwd()+F.ls()[0])                                           # 11 
#r=_                                                                    # 12 
#_13=r.text                                                             # 13 
#_14=r.headers                                                          # 14 
#_15=dict(r.headers)                                                    # 15 
#_16=N.copy_req(r)                                                      # 16 
#import requests                                                        # 17 
#_18=requests.request(method='GET',url='https://github.com/qgb')        # 18 
#_19=requests.request(method='GET',url='https://github.com/qgb')        # 19 
#_20=requests.request(method='GET',url='https://github.com/qgb',headers={'Host': 'github.com',})  # 20 
#_21=requests.request(method='GET',url='https://github.com/qgb',headers={'Host': 'github.com',})  # 21 
#_22=requests.request(method='GET',url='https://github.com/qgb',headers={'Host': 'github.com',})  # 22 
#headers=                                                               # 23 
#_24={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 YaBrowser/19.3.1.779 Yowser/2.5 Safari/537.36',
 'Accept-Encoding': 'gzip, deflate, br',
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Connection': 'close',
 'Content-Type': '',
 'Host': 'github.com',
 'X-Real-Ip': '106.19.199.164',
 'X-Forwarded-For': '106.19.199.164',
 'Upgrade-Insecure-Requests': '1',
 'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
 'Cookie': 'OGPC=19022591-2:; _ga=GA1.2.260884278.1618422125; __Host-GAPS=1:-1sTChkO5pcr8-jZftsoy1ADoMI2ww:EM_lQiLjaH0YNXRI; zhwiktionarywmE-sessionTickLastTickTime=1618425564384; zhwiktionarywmE-sessionTickTickCount=3; zhwiktionaryel-sessionId=17141c0c664050879453; _ga=GA1.3.260884278.1618422125; zhwikiwmE-sessionTickLastTickTime=1618507142883; zhwikiwmE-sessionTickTickCount=1; zhwikiel-sessionId=9be61cb5425bb68d6b27'
 }                                                                      # 24 
#_25=requests.request(method='GET',url='https://github.com/qgb',headers={'Host': 'github.com',})  # 25 
#_26=requests.request(method='GET',url='https://github.com/qgb',headers=_24)  # 26 
#_27=U.pop_dict_multi_key(_24,'Cookie','Upgrade-Insecure-Requests',)    # 27 
#_28=_24                                                                # 28 
#_29=requests.request(method='GET',url='https://github.com/qgb',headers=_24)  # 29 
#_30=requests.request(method='GET',url='https://github.com/qgb',headers=_24)  # 30 
#U.pop_dict_multi_key(_24+_27,'Cookie','Upgrade-Insecure-Requests',)    # 31 
#_24.update(_27)                                                        # 32 
#_33=_24                                                                # 33 
#U.pop_dict_multi_key(_24+_27,'Cookie','Upgrade-Insecure-Requests','X-Forwarded-For','X-Real-Ip','Connection')  # 34 
#_35=U.pop_dict_multi_key(_24,'Cookie','Upgrade-Insecure-Requests','X-Forwarded-For','X-Real-Ip','Connection')  # 35 
#_36=requests.request(method='GET',url='https://github.com/qgb',headers=_24)  # 36 
#_37=U.pop_dict_multi_key(_24,'Cookie','Upgrade-Insecure-Requests','X-Forwarded-For','X-Real-Ip','Connection')  # 37 
#_38=U.pop_dict_multi_key(_24,'Cookie','Upgrade-Insecure-Requests','X-Forwarded-For','X-Real-Ip','Connection',)  # 38 
#_39=U.pop_dict_multi_key(_24,'Cookie','Upgrade-Insecure-Requests','X-Forwarded-For','X-Real-Ip','Connection','Accept','Accept-Encoding','Accept-Language')  # 39 
#_40=_24                                                                # 40 
#_41=requests.request(method='GET',url='https://github.com/qgb',headers=_24)  # 41 
#_42=requests.request(method='GET',url='https://github.com/qgb',headers=_24)  # 42 
#_43=U.pop_dict_multi_key(_24,'Cookie','Upgrade-Insecure-Requests','X-Forwarded-For','X-Real-Ip','Connection','Accept','Accept-Encoding','Accept-Language','Content-Type')  # 43 
#_44=requests.request(method='GET',url='https://github.com/qgb',headers=_24)  # 44 
#_45=requests.request(method='GET',url='https://github.com/qgb',headers=_24)  # 45 
#_46={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 YaBrowser/19.3.1.779 Yowser/2.5 Safari/537.36',
 'Accept-Encoding': 'gzip, deflate, br',
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Connection': 'close',
 'Content-Type': '',
 'Host': 'github.com',
 'X-Real-Ip': '106.19.199.164',
 'X-Forwarded-For': '106.19.199.164',
 'Upgrade-Insecure-Requests': '1',
 'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
 'Cookie': 'OGPC=19022591-2:; _ga=GA1.2.260884278.1618422125; __Host-GAPS=1:-1sTChkO5pcr8-jZftsoy1ADoMI2ww:EM_lQiLjaH0YNXRI; zhwiktionarywmE-sessionTickLastTickTime=1618425564384; zhwiktionarywmE-sessionTickTickCount=3; zhwiktionaryel-sessionId=17141c0c664050879453; _ga=GA1.3.260884278.1618422125; zhwikiwmE-sessionTickLastTickTime=1618507142883; zhwikiwmE-sessionTickTickCount=1; zhwikiel-sessionId=9be61cb5425bb68d6b27'
 }                                                                      # 46 
#_47=U.pop_dict_multi_key(_46,'Upgrade-Insecure-Requests','X-Forwarded-For','X-Real-Ip','Connection','Accept','Accept-Encoding','Accept-Language','Content-Type')  # 47 
#_48=_46                                                                # 48 
#_49=requests.request(method='GET',url='https://github.com/qgb',headers=_46)  # 49 
#_50={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 YaBrowser/19.3.1.779 Yowser/2.5 Safari/537.36',
 'Accept-Encoding': 'gzip, deflate, br',
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Connection': 'close',
 'Content-Type': '',
 'Host': 'github.com',
 'X-Real-Ip': '106.19.199.164',
 'X-Forwarded-For': '106.19.199.164',
 'Upgrade-Insecure-Requests': '1',
 'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
 'Cookie': 'OGPC=19022591-2:; _ga=GA1.2.260884278.1618422125; __Host-GAPS=1:-1sTChkO5pcr8-jZftsoy1ADoMI2ww:EM_lQiLjaH0YNXRI; zhwiktionarywmE-sessionTickLastTickTime=1618425564384; zhwiktionarywmE-sessionTickTickCount=3; zhwiktionaryel-sessionId=17141c0c664050879453; _ga=GA1.3.260884278.1618422125; zhwikiwmE-sessionTickLastTickTime=1618507142883; zhwikiwmE-sessionTickTickCount=1; zhwikiel-sessionId=9be61cb5425bb68d6b27'
 }                                                                      # 50 
#_51=U.pop_dict_multi_key(_,'Upgrade-Insecure-Requests','X-Forwarded-For','X-Real-Ip','Connection','Content-Type')  # 51 
#_52=requests.request(method='GET',url='https://github.com/qgb',headers=_50)  # 52 
#_53={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 YaBrowser/19.3.1.779 Yowser/2.5 Safari/537.36',
 'Accept-Encoding': 'gzip, deflate, br',
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Connection': 'close',
 'Content-Type': '',
 'Host': 'github.com',
 'X-Real-Ip': '106.19.199.164',
 'X-Forwarded-For': '106.19.199.164',
 'Upgrade-Insecure-Requests': '1',
 'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
 'Cookie': 'OGPC=19022591-2:; _ga=GA1.2.260884278.1618422125; __Host-GAPS=1:-1sTChkO5pcr8-jZftsoy1ADoMI2ww:EM_lQiLjaH0YNXRI; zhwiktionarywmE-sessionTickLastTickTime=1618425564384; zhwiktionarywmE-sessionTickTickCount=3; zhwiktionaryel-sessionId=17141c0c664050879453; _ga=GA1.3.260884278.1618422125; zhwikiwmE-sessionTickLastTickTime=1618507142883; zhwikiwmE-sessionTickTickCount=1; zhwikiel-sessionId=9be61cb5425bb68d6b27'
 }                                                                      # 53 
#_54=U.pop_dict_multi_key(_,'Content-Type')                             # 54 
#_55=_53                                                                # 55 
#_56=requests.request(method='GET',url='https://github.com/qgb',headers=_53)  # 56 
#_57=requests.request(method='GET',url='https://github.com/qgb',headers=_53)  # 57 
#_58=requests.request(method='GET',url='https://github.com/qgb',headers=_53)  # 58 
#_59=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 59 
#get_ipython().magic('ls ')                                             # 60 
#get_ipython().magic('rm *')                                            # 61 
#get_ipython().magic('ls ')                                             # 62 
#_63=F.dl( U.pwd()+F.ls()[0])                                           # 63 
#r=_                                                                    # 64 
#_65=dict(r.request.headers)                                            # 65 
#_66=N.copy_req(r)                                                      # 66 
#_67=requests.request(method='GET',url='https://github.com/qgb',headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 YaBrowser/19.3.1.779 Yowser/2.5 Safari/537.36',
 'Accept-Encoding': 'gzip, deflate, br',
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Connection': 'close',
 'Content-Type': '',
 'Host': 'github.com',
 'X-Real-Ip': '106.19.199.164',
 'X-Forwarded-For': '106.19.199.164',
 'Cache-Control': 'max-age=0',
 'Upgrade-Insecure-Requests': '1',
 'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
 'Cookie': 'OGPC=19022591-2:; _ga=GA1.2.260884278.1618422125; __Host-GAPS=1:-1sTChkO5pcr8-jZftsoy1ADoMI2ww:EM_lQiLjaH0YNXRI; zhwiktionarywmE-sessionTickLastTickTime=1618425564384; zhwiktionarywmE-sessionTickTickCount=3; zhwiktionaryel-sessionId=17141c0c664050879453; _ga=GA1.3.260884278.1618422125; zhwikiwmE-sessionTickLastTickTime=1618507142883; zhwikiwmE-sessionTickTickCount=1; zhwikiel-sessionId=9be61cb5425bb68d6b27'
 },)                                                                    # 67 
#_68={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 YaBrowser/19.3.1.779 Yowser/2.5 Safari/537.36',
'Accept-Encoding': 'gzip, deflate, br',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Connection': 'close',
'Content-Type': '',
'Host': 'github.com',
'X-Real-Ip': '106.19.199.164',
'X-Forwarded-For': '106.19.199.164',
'Cache-Control': 'max-age=0',
'Upgrade-Insecure-Requests': '1',
'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
'Cookie': 'OGPC=19022591-2:; _ga=GA1.2.260884278.1618422125; __Host-GAPS=1:-1sTChkO5pcr8-jZftsoy1ADoMI2ww:EM_lQiLjaH0YNXRI; zhwiktionarywmE-sessionTickLastTickTime=1618425564384; zhwiktionarywmE-sessionTickTickCount=3; zhwiktionaryel-sessionId=17141c0c664050879453; _ga=GA1.3.260884278.1618422125; zhwikiwmE-sessionTickLastTickTime=1618507142883; zhwikiwmE-sessionTickTickCount=1; zhwikiel-sessionId=9be61cb5425bb68d6b27'
}                                                                       # 68 
#U.stime)(                                                              # 69 
#_70=U.stime()                                                          # 70 
#_71=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 71 
#get_ipython().magic('rm *')                                            # 72 
#get_ipython().magic('ls ')                                             # 73 
#get_ipython().magic('ls ')                                             # 74 
#get_ipython().magic('ls ')                                             # 75 
#_76=[U.pwd()+i for i in F.ls() if 'tab-3D' in i]                       # 76 
#f=_[0]                                                                 # 77 
#_78=f                                                                  # 78 
#_79=F.dl(f)                                                            # 79 
#r=_                                                                    # 80 
#LEN r.content                                                          # 81 
#_82=len(r.content)                                                     # 82 
#_83=F.dl(0)                                                            # 83 
#_84=F.dp(r.content,'/home/klk/test/0.dill')                            # 84 
#_85=[U.pwd()+i for i in F.ls() if 'tab-3D' in i]                       # 85 
#f=_[1]                                                                 # 86 
#r=F.dl( f)                                                             # 87 
#_88=F.dp(r.content,'/home/klk/test/0.dill')                            # 88 
#[U.pwd()+i for i in F.ls() if U.input_set(U.pwd()) in i]               # 89 
#_90=U.input_set(U.pwd())                                               # 90 
#_91=U.input_set(U.pwd())                                               # 91 
#_92=U.input_set(U.pwd())                                               # 92 
#get_ipython().magic('debug U.input_set(U.pwd())')                      # 93 
#get_ipython().magic('debug U.input_set(U.pwd())')                      # 94 
#_95=U.input(0,3232)                                                    # 95 
#_96=U.input(0,3232)                                                    # 96 
#_97=U._useless_win_input('123','4343')                                 # 97 
#_98=U._useless_win_input('123','4343')                                 # 98 
#_99=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 99 
#_100=U.input(0,3232)                                                   # 100 
#_101=3232                                                              # 101 
#_102=3232                                                              # 102 
#_103=3232                                                              # 103 
#_104=3232                                                              # 104 
#_105=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 105 
#_106=3232                                                              # 106 
#_107=U.input(0,3232)                                                   # 107 
#_108=U.input(0,3232)                                                   # 108 
#get_ipython().magic('debug U.input_set(U.pwd())')                      # 109 
#[U.pwd()+i for i in F.ls() if U.input_set(U.pwd()) in i]               # 110 
#_111=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 111 
#[U.pwd()+i for i in F.ls() if U.input_set(U.pwd()) in i]               # 112 
#[U.pwd()+i for i in F.ls() if U.get_input(id(_)) in i]                 # 113 
#_114=[U.pwd()+i for i in F.ls() if U.get_or_input(id(_)) in i]         # 114 
#f=_[1]                                                                 # 115 
#f=_[0]                                                                 # 116 
#r=F.dl( f)                                                             # 117 
#_118=F.dp(r.content,'/home/klk/test/0.dill')                           # 118 
#s=r.text                                                               # 119 
#_120=F.dp(r.text,1)                                                    # 120 
#get_ipython().system('curl https://klk.pythonanywhere.com/-r=233')     # 121 
#T.r                                                                    # 122 
#_123=U.cdt()                                                           # 123 
#_124=F.ls()                                                            # 124 
#f=_[-1]                                                                # 125 
#_126=f                                                                 # 126 
#ws=F.dl(F.ls()[-1])                                                    # 127 
#_128=len(ws)                                                           # 128 
#_129=U.searchIterable(ws,'github')                                     # 129 
#File "D:\XX-Net\python3.8.2\lib\urllib\request.py", line 1362, in https_open  # 130 
#get_ipython().system('curl -vvi https://github.githubassets.com/assets/chunk-tweetsodium-be01c912.js')  # 131 
#_132=U.searchIterable(ws,'proxy')                                      # 132 
#get_ipython().system('curl -vvi https://api.proxycrawl.com?url=https://github.githubassets.com/assets/chunk-tweetsodium-be01c912.js')  # 133 
#curl 'https://api.proxycrawl.com/?token=rk8LVh_j_FTKsgLSzbZu-g&url=https%3A%2F%2Fwww.amazon.com'  # 134 
#get_ipython().system("curl 'https://api.proxycrawl.com/?token=rk8LVh_j_FTKsgLSzbZu-g&url=https%3A%2F%2Fwww.amazon.com'")  # 135 
#_136=len(s)                                                            # 136 
#b=T.BeautifulSoup(s)                                                   # 137 
#b.select('[*=http]')                                                   # 138 
#b.select('[*=http]')                                                   # 139 
#attrs=[]                                                               # 140 
#for v in b.find_all():
 v                                                                      # 141 
#_142=U.len(b())                                                        # 142 
#for v in b.find_all():
 attrs+=list(v.attrs.values())                                          # 143 
#_144=len(attrs)                                                        # 144 
#_145=U.unique(U.type(*attrs))                                          # 145 
#_146=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 146 
#_147=U.unique(U.type(*attrs),d=1)                                      # 147 
#F.dp()                                                                 # 148 
#_149=F.dp(attrs,0)                                                     # 149 
#r=F.dp(attrs,0)                                                        # 150 
#_151=len(r)                                                            # 151 
#F.dp(r.content,'/home/klk/test/0.dill')                                # 152 
#r=F.dl( f)                                                             # 153 
#_154=F.dp([],0)                                                        # 154 
#_155=F.dp(attrs,2)                                                     # 155 
#curl gstatic.com                                                       # 156 
#get_ipython().system('curl gstatic.com')                               # 157 
#_158=U.searchIterable(ws,'past')                                       # 158 
#get_ipython().magic('ls ')                                             # 159 
#_160=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 160 
#_161=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 161 
#_162=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 162 
#_163=U.searchIterable(ws,'*')                                          # 163 
#_164=T.regexMatch(s,'(?<=")http')                                      # 164 
#_165=T.regexMatchAll(s,'(?<=")http')                                   # 165 
#_166=T.regexMatchAll(s,'(?<=\")http.*')                                # 166 
#T.regexMatchAll(s,'(?<=\")http.*(?>=\")')                              # 167 
#_168=T.regexMatchAll(s,'(?<=\")http.*(?<=\")')                         # 168 
#_169=T.regexMatchAll(s,'(?<=\")http.*(?=\")')                          # 169 
#_170=T.regexMatchAll(s,'(?<=\")http.*(?=\")')                          # 170 
#_171=T.regexMatchAll(s,r'(?<=\")http.*?(?=\")')                        # 171 
#_172=len(_)                                                            # 172 
#_173=ipy.save(_i171)                                                   # 173 
#_174=len(T.regexMatchAll(s,r'(?<=\")http.*?(?=\")'))                   # 174 
#_175=len(T.regexMatchAll(s,r'(?<=\=\")http.*?(?=\")'))                 # 175 
#_176=len(T.regexMatchAll(s,r'(?<=\=\")http.*?(?=\")'))                 # 176 
#_177=len(T.regexMatchAll(s,r'(?<=\")http.*?(?=\")'))                   # 177 
#ipy.save()                                                             # 178 
