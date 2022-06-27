#coding=utf-8
import sys;'qgb.U' in sys.modules or sys.path.append('/home/klk/');from qgb import *

#U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 1 
#from qgb import *                                                      # 2 
#_3=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 3 
#from qgb import *,git                                                  # 4 
from qgb import git                                                     # 5 
#_6=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 6 
from qgb import git                                                     # 7 
#_8=get_ipython().run_line_magic('pwd', '')                             # 8 
fs=F.ls(U.pwd,r=1)                                                      # 9 
_10=fs[4]                                                               ;"""#10
'net-tools-1.60/'
"""
_11=len(fs)                                                             ;"""#11
13416
"""
#get_ipython().run_line_magic('ll', '')                                 # 12 
fs=F.ls(U.pwd(),r=1)                                                    # 13 
_14=fs[4]                                                               ;"""#14
'/home/klk/net-tools-1.60/'
"""
_15=len(fs)                                                             ;"""#15
13416
"""
_16=U.len(f for f in fs if f.endswith('/'))                             ;"""#16
1165
"""
fs=F.ls(U.pwd(),r=1,f=1)                                                # 17 
_18=len(fs)                                                             ;"""#18
12251
"""
_19=_+__                                                                ;"""#19
13416
"""
for f in U.progressbar(fs):
    f                                                                   # 20 
#get_ipython().run_line_magic('pinfo', 'U.progressbar')                 # 21 
#get_ipython().run_line_magic('pinfo2', 'U.progressbar')                # 22 
#get_ipython().run_line_magic('pip', 'install progressbar2')            # 23 
for f in U.progressbar(fs[:22]):
    U.p(f,' ')                                                          # 24 
for n,f in enumerate(fs[:22]):
    U.p(f,' ')                                                          # 25 
for n,f in enumerate(fs[:22]):
    U.p(n,f[-44:],' ')                                                  # 26 
_27=T.enu(T.az*4)                                                       ;"""#27
'0         1         2         3         4         5         6         7         8         9         \n01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123\nabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz\n'
"""
T.enu(T.az*4,p=1)                                                       # 28 
T.enu(T.az*6,p=1)                                                       # 29 
T.enu(T.az*6[:143],p=1)                                                 # 30 
T.enu((T.az*6)[:143],p=1)                                               # 31 
T.enu((T.az*6)[:144],p=1)                                               # 32 
for n,f in enumerate(fs[:22]):
    U.p('%5s'%n+f[-5:])                                                 # 33 
for n,f in enumerate(fs[:22]):
    U.p('%5s'%n+f[-4:])                                                 # 34 
_35=len(fs)                                                             ;"""#35
12251
"""
#ipy.dump(fs)                                                           # 36 
#get_ipython().run_line_magic('ll', '')                                 # 37 
#get_ipython().run_line_magic('rm', 'python3.vp2.2792110')              # 38 
#ipy.dump(fs)                                                           # 39 
_40=len(fs)                                                             ;"""#40
12251
"""
fs=F.ls(U.pwd(),r=1,f=1)                                                # 41 
_42=len(fs)                                                             ;"""#42
12253
"""
#get_ipython().run_line_magic('ll', '')                                 # 43 
#get_ipython().system('disk -l')                                        # 44 
#get_ipython().system('df -h')                                          # 45 
#get_ipython().system('du -m|sort -n|tail -n 99')                       # 46 
#get_ipython().run_line_magic('ll', '')                                 # 47 
#get_ipython().run_line_magic('ll', '-alh')                             # 48 
#get_ipython().run_line_magic('rm', '-rf .cache')                       # 49 
#_50=ipy.dump(fs)                                                       # 50 
_51=F.delete(_)                                                         ;"""#51
'/home/klk/test/fs-12253.dill'
"""
fs=F.ls(U.pwd(),r=1,f=1)                                                # 52 
_53=len(fs)                                                             ;"""#53
12187
"""
#_54=ipy.dump(fs)                                                       # 54 
fs=F.ls(U.pwd(),r=1,f=1)                                                # 55 
_56=fs=F.ls(U.pwd(),r=1,f=1);len(fs)                                    ;"""#56
12188
"""
#_57=ipy.dump(fs)                                                       # 57 
_58=fs=F.ls(U.pwd(),r=1,f=1);len(fs)                                    ;"""#58
12189
"""
_59=F.delete(_54)                                                       ;"""#59
'/home/klk/test/fs-12187.dill'
"""
_60=fs=F.ls(U.pwd(),r=1,f=1);len(fs)                                    ;"""#60
12188
"""
#_61=ipy.dump(fs)                                                       # 61 
_62=fs=F.ls(U.pwd(),r=1,f=1);len(fs)                                    ;"""#62
12188
"""
for n,f in enumerate(fs[:22]):
    U.p('%5s'%n+f[-4:])                                                 # 63 
for n,f in enumerate(fs[:22]):
    U.p('%5s'%n+f[-11:])                                                # 64 
_65=fs=F.ls(U.pwd(),r=1,f=1);len(fs)                                    ;"""#65
12188
"""
#get_ipython().run_line_magic('clear', '')                              # 66 
for n,f in enumerate(fs):
    U.p('%5s'%n+f[-11:])                                                # 67 
#get_ipython().run_line_magic('clear', '')                              # 68 
for n,f in enumerate(fs):
    U.p('%5s'%n+f[-11:])
    
    break                                                               # 69 
_70=git.github_upload(f)                                                ;"""#70
<Response [201]>
"""
for n,f in enumerate(fs):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if r.status_code!=201:
        print(r)
        break                                                           # 71 
print(r.text)                                                           # 72 
print(r.json())                                                         # 73 
print(r.json()['message'])                                              # 74 
for n,f in enumerate(fs):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if r.status_code!=201:
        print(r)
        break
        
    break                                                               # 75 
for n,f in enumerate(fs):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if r.status_code!=201:
        print(r)
        break
        
    break                                                               # 76 
print(U.stime())
for n,f in enumerate(fs):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if r.status_code!=201:
        print(r)
        break
    if U.itime()%(5*60)==0:print(U.stime())    
    #break                                                              # 77 
filename                                                                # 78 
_79=f                                                                   ;"""#79
'/home/klk/dstat-0.7.2/examples/dstat.py'
"""
_80=F.read_byte(f)                                                      ;"""#80
		###<py.No|FileNotFoundError(2, 'No such file or directory'),'/home/klk/dstat-0.7.2/examples/dstat.py'  2022-06-25__07.33.35__>
"""
#get_ipython().run_line_magic('ls', 'f')                                # 81 
_82=F.size(f)                                                           ;"""#82
		###<py.No|'/home/klk/dstat-0.7.2/examples/dstat.py NOT EXISTS!'  2022-06-25__07.33.46__>
"""
#get_ipython().run_line_magic('ll', '-al /home/klk/dstat-0.7.2/examples/dstat.py')  # 83 
_84=fs=F.ls(U.pwd(),r=1,f=1);len(fs)                                    ;"""#84
12204
"""
fs12204=fs                                                              # 85 
#_86=ipy.outType(str)                                                   # 86 
#_87=ipy.input('ipy.dump')                                              # 87 
_88=_61                                                                 ;"""#88
'/home/klk/test/fs-12188.dill'
"""
#get_ipython().run_line_magic('rm', '{_61)')                            # 89 
#get_ipython().run_line_magic('rm', '{_61}')                            # 90 
#get_ipython().run_line_magic('ls', '/home/klk/test/fs*')               # 91 
_92=fs=F.ls(U.pwd(),r=1,f=1);len(fs)                                    ;"""#92
12204
"""
#get_ipython().run_line_magic('rm', '/home/klk/test/fs-12251.dill')     # 93 
_94=fs=F.ls(U.pwd(),r=1,f=1);len(fs)                                    ;"""#94
12203
"""
_95=fs=F.ls(U.pwd(),r=1,f=1);len(fs)                                    ;"""#95
12203
"""
fs.append(len(fs))                                                      # 96 
#_97=ipy.dump(fs)                                                       # 97 
_98=fs=F.ls(U.pwd(),r=1,f=1);len(fs)                                    ;"""#98
12204
"""
#_99=ipy.dump(fs)                                                       # 99 
#get_ipython().run_line_magic('clear', '')                              # 100 
os.path.islink(path)                                                    # 101 
_102=f                                                                  ;"""#102
'/home/klk/dstat-0.7.2/examples/dstat.py'
"""
os.path.islink(f)                                                       # 103 
#import sys,os;'qgb.U' in sys.modules or sys.path.append('/home/klk/');from qgb import *  # 104 
_105=os.path.islink(f)                                                  ;"""#105
True
"""
_106=fs=[i for i in F.ls(U.pwd(),r=1,f=1) if '/qgb/.git/' not in i];len(fs)  ;"""#106
11344
"""
#_107=ipy.input('ipy.dump')                                             # 107 
_108=_99                                                                ;"""#108
'/home/klk/test/fs-12204.dill'
"""
#get_ipython().run_line_magic('rm', '{_}')                              # 109 
#get_ipython().run_line_magic('ls', '/home/klk/test/fs*')               # 110 
_111=fs=[i for i in F.ls(U.pwd(),r=1,f=1) if '/qgb/.git/' not in i];len(fs)  ;"""#111
11343
"""
#_112=fs.append(len(fs));ipy.dump(fs)                                   # 112 
_113=fs=[i for i in F.ls(U.pwd(),r=1,f=1) if '/qgb/.git/' not in i];len(fs)  ;"""#113
11344
"""
#_114=ipy.dump(fs)                                                      # 114 
#_115=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py)
U.cdb()                                                                 # 115 
#_116=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 116 
_117=len(fs)                                                            ;"""#117
11344
"""
_118=fs=[i for i in F.ls(U.pwd(),r=1,f=1) if '/qgb/.git/' not in i];len(fs)  ;"""#118
11344
"""
#_119=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 119 
claer                                                                   # 120 
#get_ipython().run_line_magic('clear', '')                              # 121 
_122=fs=[i for i in F.ls(U.pwd(),r=1,f=1) if '/qgb/.git/' not in i];len(fs)  ;"""#122
11344
"""
print(U.stime())
for n,f in enumerate(fs):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if not r:r=r.a
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 123 
_124=r                                                                  ;"""#124
<Response [400]>
"""
print(r.json()['message'])                                              # 125 
U.r(U,T,N,N.HTTP,F,py);                                                 # 126 
#_127=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 127 
print(U.stime())
for n,f in enumerate(fs):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):r=r.a
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 128 
#_129=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 129 
_130=f                                                                  ;"""#130
'/home/klk/dstat-0.7.2/examples/dstat.py'
"""
git.github_upload(f)                                                    # 131 
#_132=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 132 
_133=git.github_upload(f)                                               ;"""#133
		###<py.No|'/home/klk/dstat-0.7.2/examples/dstat.py','symlink'  2022-06-25__07.55.31__>
"""
_134=_.a                                                                ;"""#134
('/home/klk/dstat-0.7.2/examples/dstat.py', 'symlink')
"""
#_135=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 135 
_136=git.github_upload(f)                                               ;"""#136
		###<py.No|'link','/home/klk/dstat-0.7.2/examples/dstat.py'  2022-06-25__07.57.24__>
"""
_137=fs.index(f)                                                        ;"""#137
77
"""
_138=fs[77:79]                                                          ;"""#138
['/home/klk/dstat-0.7.2/examples/dstat.py',
 '/home/klk/dstat-0.7.2/examples/devtest.py']
"""
print(U.stime())
for n,f in enumerate(fs[77:]):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):r=r.a
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 139 
print(U.stime())
for n,f in enumerate(fs[77:]):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):
        U.print_repr(r)
        continue
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 140 
_141=f                                                                  ;"""#141
'/home/klk/v/.git/refs/heads/master'
"""
#get_ipython().run_line_magic('ll', '-al {f}')                          # 142 
_143=F.read_byte(f)                                                     ;"""#143
b'234820a25edef263f18db9b9e3778ff012dd6ea1\n'
"""
_144=git.github_upload(f)                                               ;"""#144
<Response [422]>
"""
_145=r                                                                  ;"""#145
<Response [422]>
"""
print(r.json()['message'])                                              # 146 
_147=r.json()                                                           ;"""#147
{'message': 'path contains a malformed path component',
 'errors': [{'resource': 'Commit', 'field': 'path', 'code': 'invalid'}],
 'documentation_url': 'https://docs.github.com/rest/reference/repos#create-or-update-file-contents'}
"""
_148=fs.index(f)                                                        ;"""#148
278
"""
_149=n=278;fs[n:n+9]                                                    ;"""#149
['/home/klk/v/.git/refs/heads/master',
 '/home/klk/v/.git/refs/remotes/origin/HEAD',
 '/home/klk/v/.git/logs/refs/heads/master',
 '/home/klk/v/.git/logs/refs/remotes/origin/HEAD',
 '/home/klk/v/.git/logs/HEAD',
 '/home/klk/v/.git/objects/23/721cb99b6d11c6a0b7b3bf2d459efcfc562bd7',
 '/home/klk/v/.git/objects/23/4820a25edef263f18db9b9e3778ff012dd6ea1',
 '/home/klk/v/.git/objects/e3/128bf2c58097ea282e7249e6dafad670bf49d1',
 '/home/klk/v/.git/objects/9d/f7cb8fcc818aa7d74955fa46235c533e5d7768']
"""
_150=fs[291]                                                            ;"""#150
'/home/klk/v/.git/hooks/pre-push.sample'
"""
_151=git.github_upload(_150)                                            ;"""#151
<Response [422]>
"""
_152=fs=[i for i in F.ls(U.pwd(),r=1,f=1) if '/.git/' not in i];len(fs)  ;"""#152
11318
"""
#_153=ipy.dump(fs)                                                      # 153 
#get_ipython().run_line_magic('rm', '{_}')                              # 154 
_155=fs=[i for i in F.ls(U.pwd(),r=1,f=1) if '/.git/' not in i];len(fs)  ;"""#155
11318
"""
#_156=fs.append(len(fs));ipy.dump(fs)                                   # 156 
_157=fs=[i for i in F.ls(U.pwd(),r=1,f=1) if '/.git/' not in i];len(fs)  ;"""#157
11319
"""
_158=n=278;fs[n:n+9]                                                    ;"""#158
['/home/klk/v/htop',
 '/home/klk/v/syncthing-windows-amd64-v1.19.1.zip',
 '/home/klk/v/python3.vp2',
 '/home/klk/v/control_flow_v9.3_20210404.py',
 '/home/klk/v/python3.6',
 '/home/klk/test/webcache.googleusercontent.com/Gsearch-3Fq-3Dcache-3AwMfqaWk8AxUJ-3Amfyq.com.cn-252F-253Fs-253Dmonog_de-2526id-253D6-2B-26cd-3D8-26hl-3Dzh-2DCN-26ct-3Dclnk-26gl-3Dus.dill',
 '/home/klk/test/webcache.googleusercontent.com/Pgen_204-3Fatyp-3Dcsi-26ei-3DISp3YJuDAu-2Dz5NoP3Lyd6AU-26s-3Djsa-26jsi-3Ds-2Cst.351648-2Ctni.0-2Cet.click-2Cve.2ahUKEwjbl9r0pP7vAhXvGVkFHVxeB10Q7B0wB3oECAkQBg-2Cn.hiU8Ie-2Ccn.6-26zx-3D1618422672880.dill',
 '/home/klk/test/webcache.googleusercontent.com/Gsearch-3Fq-3D-2Da-253DN.geta-28q-29-253Br-253Dconfig-28-27https-253A-252F-27-252Bchr-2847-29-252Ba-29-253B-252523-2Dwww.google.com.dill',
 '/home/klk/test/webcache.googleusercontent.com/Pgen_204-3Fatyp-3Di-26ei-3DISp3YJuDAu-2Dz5NoP3Lyd6AU-26ved-3D2ahUKEwjbl9r0pP7vAhXvGVkFHVxeB10Q7B0wB3oECAkQBg-26vet-3D12ahUKEwjbl9r0pP7vAhXvGVkFHVxeB10QqR8wB3oECAkQBw..s-26zx-3D1618422672886.dill']
"""
#get_ipython().run_line_magic('ll', '')                                 # 159 
#get_ipython().run_line_magic('rm', '-rf v')                            # 160 
_161=fs=[i for i in F.ls(U.pwd(),r=1,f=1) if '/.git/' not in i];len(fs)  ;"""#161
11314
"""
#_162=fs.append(len(fs));ipy.dump(fs)                                   # 162 
#_163=fs.append(len(fs));ipy.dump(fs)                                   # 163 
#get_ipython().run_line_magic('rm', '-rf v')                            # 164 
#get_ipython().run_line_magic('rm', '{_}')                              # 165 
_166=fs=[i for i in F.ls(U.pwd(),r=1,f=1) if '/.git/' not in i];len(fs)  ;"""#166
11315
"""
for n,f in enumerate(fs):
    if '/qgb/' not in f:continue
    print(n,f)                                                          # 167 
_168=fs[277:]                                                           ;"""#168
#Warning#  len(pout)=348479 > out_max
"""
#get_ipython().run_line_magic('clear', '')                              # 169 
_170=n=278;fs[n:n+9]                                                    ;"""#170
['/home/klk/test/webcache.googleusercontent.com/Gsearch-3Fq-3Dcache-3AwMfqaWk8AxUJ-3Amfyq.com.cn-252F-253Fs-253Dmonog_de-2526id-253D6-2B-26cd-3D8-26hl-3Dzh-2DCN-26ct-3Dclnk-26gl-3Dus.dill',
 '/home/klk/test/webcache.googleusercontent.com/Pgen_204-3Fatyp-3Dcsi-26ei-3DISp3YJuDAu-2Dz5NoP3Lyd6AU-26s-3Djsa-26jsi-3Ds-2Cst.351648-2Ctni.0-2Cet.click-2Cve.2ahUKEwjbl9r0pP7vAhXvGVkFHVxeB10Q7B0wB3oECAkQBg-2Cn.hiU8Ie-2Ccn.6-26zx-3D1618422672880.dill',
 '/home/klk/test/webcache.googleusercontent.com/Gsearch-3Fq-3D-2Da-253DN.geta-28q-29-253Br-253Dconfig-28-27https-253A-252F-27-252Bchr-2847-29-252Ba-29-253B-252523-2Dwww.google.com.dill',
 '/home/klk/test/webcache.googleusercontent.com/Pgen_204-3Fatyp-3Di-26ei-3DISp3YJuDAu-2Dz5NoP3Lyd6AU-26ved-3D2ahUKEwjbl9r0pP7vAhXvGVkFHVxeB10Q7B0wB3oECAkQBg-26vet-3D12ahUKEwjbl9r0pP7vAhXvGVkFHVxeB10QqR8wB3oECAkQBw..s-26zx-3D1618422672886.dill',
 '/home/klk/test/webcache.googleusercontent.com/Gurl-3Fsa-3Dt-26rct-3Dj-26q-3D-26esrc-3Ds-26source-3Dweb-26cd-3D-26cad-3Drja-26uact-3D8-26ved-3D2ahUKEwjbl9r0pP7vAhXvGVkFHVxeB10QIDAHegQICRAI-26url-3Dhttp-253A-252F-252Fwebcache.googleusercontent.com-252Fsearch-253Fq-253Dcache-253AwMfqaWk8AxUJ-253Amf.dill',
 '/home/klk/test/fifo/cmd',
 '/home/klk/test/ipy/z.py',
 '/home/klk/test/ipy/2021-04-30__05.32.49__.341.py',
 "/home/klk/test/ipy/T.regexMatchAll(h,'[a-z.：／]＊gstatic.com[／＼w.]＊').py"]
"""
_171=n=277;fs[n:n+9]                                                    ;"""#171
['/home/klk/qgb/boot.py',
 '/home/klk/test/webcache.googleusercontent.com/Gsearch-3Fq-3Dcache-3AwMfqaWk8AxUJ-3Amfyq.com.cn-252F-253Fs-253Dmonog_de-2526id-253D6-2B-26cd-3D8-26hl-3Dzh-2DCN-26ct-3Dclnk-26gl-3Dus.dill',
 '/home/klk/test/webcache.googleusercontent.com/Pgen_204-3Fatyp-3Dcsi-26ei-3DISp3YJuDAu-2Dz5NoP3Lyd6AU-26s-3Djsa-26jsi-3Ds-2Cst.351648-2Ctni.0-2Cet.click-2Cve.2ahUKEwjbl9r0pP7vAhXvGVkFHVxeB10Q7B0wB3oECAkQBg-2Cn.hiU8Ie-2Ccn.6-26zx-3D1618422672880.dill',
 '/home/klk/test/webcache.googleusercontent.com/Gsearch-3Fq-3D-2Da-253DN.geta-28q-29-253Br-253Dconfig-28-27https-253A-252F-27-252Bchr-2847-29-252Ba-29-253B-252523-2Dwww.google.com.dill',
 '/home/klk/test/webcache.googleusercontent.com/Pgen_204-3Fatyp-3Di-26ei-3DISp3YJuDAu-2Dz5NoP3Lyd6AU-26ved-3D2ahUKEwjbl9r0pP7vAhXvGVkFHVxeB10Q7B0wB3oECAkQBg-26vet-3D12ahUKEwjbl9r0pP7vAhXvGVkFHVxeB10QqR8wB3oECAkQBw..s-26zx-3D1618422672886.dill',
 '/home/klk/test/webcache.googleusercontent.com/Gurl-3Fsa-3Dt-26rct-3Dj-26q-3D-26esrc-3Ds-26source-3Dweb-26cd-3D-26cad-3Drja-26uact-3D8-26ved-3D2ahUKEwjbl9r0pP7vAhXvGVkFHVxeB10QIDAHegQICRAI-26url-3Dhttp-253A-252F-252Fwebcache.googleusercontent.com-252Fsearch-253Fq-253Dcache-253AwMfqaWk8AxUJ-253Amf.dill',
 '/home/klk/test/fifo/cmd',
 '/home/klk/test/ipy/z.py',
 '/home/klk/test/ipy/2021-04-30__05.32.49__.341.py']
"""
_172=git.github_upload(fs[277])                                         ;"""#172
<Response [422]>
"""
for n,f in enumerate(fs):
    if '/qgb/' not in f:continue
    print(n,f)                                                          # 173 
_174=fs[:122]                                                           ;"""#174
['/home/klk/dstat-0.7.2/plugins/dstat_top_cpu.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_wifi.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_cpu_adv.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_innodb_ops.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_mysql_io.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_dstat_ctxt.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_bio_adv.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_innodb_io.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_freespace.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_nfs3_ops.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_dbus.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_sendmail.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_disk_tps.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_proc_count.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_qmail.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_vz_cpu.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_gpfs.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_mem.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_bio.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_test.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_vmk_int.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_dstat_mem.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_rpcd.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_vz_ubc.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_int.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_thermal.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_mysql_keys.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_fan.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_net_packets.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_postfix.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_power.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_helloworld.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_latency_avg.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_oom.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_io_adv.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_dstat_cpu.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_ntp.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_rpc.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_memcache_hits.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_cputime.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_io.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_snooze.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_nfs3.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_cpufreq.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_squid.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_gpfs_ops.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_nfsd3.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_nfsd3_ops.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_innodb_buffer.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_battery.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_childwait.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_vm_memctl.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_lustre.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_vmk_hba.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_dstat.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_latency.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_top_cputime_avg.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_mysql5_cmds.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_utmp.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_mysql5_io.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_vmk_nic.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_battery_remain.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_disk_util.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_vz_io.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_mysql5_conn.py',
 '/home/klk/dstat-0.7.2/plugins/dstat_mysql5_keys.py',
 '/home/klk/dstat-0.7.2/debian/source/format',
 '/home/klk/dstat-0.7.2/debian/watch',
 '/home/klk/dstat-0.7.2/debian/dstat.1',
 '/home/klk/dstat-0.7.2/debian/rules',
 '/home/klk/dstat-0.7.2/debian/copyright',
 '/home/klk/dstat-0.7.2/debian/dirs',
 '/home/klk/dstat-0.7.2/debian/compat',
 '/home/klk/dstat-0.7.2/debian/control',
 '/home/klk/dstat-0.7.2/debian/docs',
 '/home/klk/dstat-0.7.2/debian/changelog',
 '/home/klk/dstat-0.7.2/examples/read.py',
 '/home/klk/dstat-0.7.2/examples/dstat.py',
 '/home/klk/dstat-0.7.2/examples/devtest.py',
 '/home/klk/dstat-0.7.2/examples/mmpipe.py',
 '/home/klk/dstat-0.7.2/examples/tdbtest',
 '/home/klk/dstat-0.7.2/examples/curstest',
 '/home/klk/dstat-0.7.2/examples/mstat.py',
 '/home/klk/dstat-0.7.2/proc/stat-2.6.11',
 '/home/klk/dstat-0.7.2/proc/partitions-2.4.21',
 '/home/klk/dstat-0.7.2/proc/diskstats-2.6.11',
 '/home/klk/dstat-0.7.2/proc/partitions-2.4.24',
 '/home/klk/dstat-0.7.2/proc/stat-2.4.24',
 '/home/klk/dstat-0.7.2/proc/stat-2.4.21',
 '/home/klk/dstat-0.7.2/proc/partitions-2.6.11',
 '/home/klk/dstat-0.7.2/.pc/.quilt_patches',
 '/home/klk/dstat-0.7.2/.pc/.quilt_series',
 '/home/klk/dstat-0.7.2/.pc/.version',
 '/home/klk/dstat-0.7.2/.pc/applied-patches',
 '/home/klk/dstat-0.7.2/docs/dstat.1.html',
 '/home/klk/dstat-0.7.2/docs/examples.html',
 '/home/klk/dstat-0.7.2/docs/Makefile',
 '/home/klk/dstat-0.7.2/docs/performance.html',
 '/home/klk/dstat-0.7.2/docs/dstat-paper.html',
 '/home/klk/dstat-0.7.2/docs/dstat-paper.txt',
 '/home/klk/dstat-0.7.2/docs/counter-rollovers.txt',
 '/home/klk/dstat-0.7.2/docs/dstat.1',
 '/home/klk/dstat-0.7.2/docs/cplugins.txt',
 '/home/klk/dstat-0.7.2/docs/examples.txt',
 '/home/klk/dstat-0.7.2/docs/screen.txt',
 '/home/klk/dstat-0.7.2/docs/screen.html',
 '/home/klk/dstat-0.7.2/docs/cplugins.html',
 '/home/klk/dstat-0.7.2/docs/counter-rollovers.html',
 '/home/klk/dstat-0.7.2/docs/performance.txt',
 '/home/klk/dstat-0.7.2/docs/dstat.1.txt',
 '/home/klk/dstat-0.7.2/dstat.spec',
 '/home/klk/dstat-0.7.2/Makefile',
 '/home/klk/dstat-0.7.2/COPYING',
 '/home/klk/dstat-0.7.2/ChangeLog',
 '/home/klk/dstat-0.7.2/AUTHORS',
 '/home/klk/dstat-0.7.2/WISHLIST',
 '/home/klk/dstat-0.7.2/dstat',
 '/home/klk/dstat-0.7.2/README',
 '/home/klk/dstat-0.7.2/LINKS',
 '/home/klk/dstat-0.7.2/dstat.conf',
 '/home/klk/dstat-0.7.2/TODO',
 '/home/klk/qgb/Win/__init__.py']
"""
l                                                                       # 175 
print(U.stime())
for n,f in enumerate(fs[278:]):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):r=r.a
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 176 
_177=n                                                                  ;"""#177
5
"""
_178=f                                                                  ;"""#178
'/home/klk/test/fifo/cmd'
"""
#get_ipython().run_line_magic('ll', '-al {f}')                          # 179 
#_180=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 180 
_181=fs[278]                                                            ;"""#181
'/home/klk/test/webcache.googleusercontent.com/Gsearch-3Fq-3Dcache-3AwMfqaWk8AxUJ-3Amfyq.com.cn-252F-253Fs-253Dmonog_de-2526id-253D6-2B-26cd-3D8-26hl-3Dzh-2DCN-26ct-3Dclnk-26gl-3Dus.dill'
"""
_182=fs.index(f)                                                        ;"""#182
283
"""
print(U.stime())
for n,f in enumerate(fs[283:]):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):r=r.a
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 183 
print(U.stime())
for n,f in enumerate(fs[283:]):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):
        U.print_repr(r)
        continue
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 184 
_185=f                                                                  ;"""#185
'/home/klk/test/ipy/z.py'
"""
#_186=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 186 
print(U.stime())
for n,f in enumerate(fs[283:]):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):
        U.print_repr(r)
        continue
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 187 
_188=f                                                                  ;"""#188
"/home/klk/test/ipy/T.regexMatchAll(h,'[a-z.：／]＊gstatic.com[／＼w.]＊').py"
"""
git.github_upload(f)                                                    # 189 
#get_ipython().run_line_magic('debug', 'git.github_upload(f)')          # 190 
#_191=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 191 
#get_ipython().run_line_magic('clear', '')                              # 192 
_193=fs[284]                                                            ;"""#193
'/home/klk/test/ipy/z.py'
"""
_194=fs[285]                                                            ;"""#194
'/home/klk/test/ipy/2021-04-30__05.32.49__.341.py'
"""
_195=fs[286]                                                            ;"""#195
"/home/klk/test/ipy/T.regexMatchAll(h,'[a-z.：／]＊gstatic.com[／＼w.]＊').py"
"""
print(U.stime())
for n,f in enumerate(fs[286:]):
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):
        U.print_repr(r)
        continue
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 196 
_197=fs[286+22]                                                         ;"""#197
'/home/klk/test/fn/"'
"""
_198=f                                                                  ;"""#198
'/home/klk/test/fn/"'
"""
_199=F.read(f)                                                          ;"""#199
'/home/klk/test/fn/"'
"""
_200=[i for i in fs if i.endswith('/')]                                 ;"""#200
[]
"""
_201=git.github_upload(f)                                               ;"""#201
<Response [400]>
"""
print(_.json()['message'])                                              # 202 
#_203=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 203 
_204=git.github_upload(f)                                               ;"""#204
<Response [201]>
"""
_205=fs[286+22]                                                         ;"""#205
'/home/klk/test/fn/"'
"""
print(U.stime())
delta=286+23
for n,f in enumerate(fs[delta:]):
    n=n+delta
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):
        U.print_repr(r)
        continue
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 206 
_207=f                                                                  ;"""#207
'/home/klk/test/fn/\\'
"""
F.read(f)                                                               # 208 
#get_ipython().run_line_magic('debug', 'F.read(f)')                     # 209 
_210=F.read_byte(f)                                                     ;"""#210
		###<py.No|IsADirectoryError(21, 'Is a directory'),'/home/klk/test/fn//'  2022-06-27__04.12.56__>
"""
#get_ipython().run_line_magic('debug', 'F.read_byte(f)')                # 211 
_212=F.gbAutoPath                                                       ;"""#212
True
"""
F.gbAutoPath=0                                                          # 213 
_214=F.auto_file_path(f)                                                ;"""#214
'/home/klk/test/fn/\\'
"""
_215=n                                                                  ;"""#215
311
"""
_216=fs[n]                                                              ;"""#216
'/home/klk/test/fn/\\'
"""
print(U.stime())
delta=311
for n,f in enumerate(fs[delta:]):
    n=n+delta
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):
        U.print_repr(r)
        continue
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 217 
_218=f                                                                  ;"""#218
'/home/klk/test/fn/#'
"""
_219=F.read_byte(f)                                                     ;"""#219
b'/home/klk/test/fn/#'
"""
_220=git.github_upload(f)                                               ;"""#220
<Response [422]>
"""
print(_.json()['message'])                                              # 221 
F.gbAutoPath=0                                                          # 222 
_223=git.github_upload(f)                                               ;"""#223
<Response [422]>
"""
#_224=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 224 
_225=git.github_upload(f,print_requests=1)                              ;"""#225
<Response [422]>
"""
requests.put('https://api.github.com:443/repos/qgbcs/kp/contents/home/klk/test/fn/%23',(b'{"message": "2022-06-27__04.22.32__.637 <19 B>/home/klk/test/fn/#", "content'
 b'": "L2hvbWUva2xrL3Rlc3QvZm4vIw==", "branch": "master"}'),headers={'Authorization': 'token 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',
 'Content-Type': 'application/json',
 'User-Agent': 'PyGithub/Python'},timeout=15,verify=True,allow_redirects=False,)  # 226 
#immport requests                                                       # 227 
import requests                                                         # 228 
_229=requests.put('https://api.github.com:443/repos/qgbcs/kp/contents/home/klk/test/fn/%23',(b'{"message": "2022-06-27__04.22.32__.637 <19 B>/home/klk/test/fn/#", "content'
 b'": "L2hvbWUva2xrL3Rlc3QvZm4vIw==", "branch": "master"}'),headers={'Authorization': 'token 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',
 'Content-Type': 'application/json',
 'User-Agent': 'PyGithub/Python'},timeout=15,verify=True,allow_redirects=False,)  ;"""#229
<Response [201]>
"""
_230=f                                                                  ;"""#230
'/home/klk/test/fn/#'
"""
_231=T.url_encode(f)                                                    ;"""#231
'/home/klk/test/fn/%23'
"""
#_232=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 232 
_233=n                                                                  ;"""#233
328
"""
print(U.stime())
delta=329
for n,f in enumerate(fs[delta:]):
    n=n+delta
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):
        U.print_repr(r)
        continue
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 234 
_235=f                                                                  ;"""#235
'/home/klk/test/fn/ '
"""
_236=git.github_upload(f,print_requests=1)                              ;"""#236
<Response [422]>
"""
_237=ord(f[-1])                                                         ;"""#237
32
"""
_238=chr(32)                                                            ;"""#238
' '
"""
#_239=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 239 
_240=git.github_upload(f,print_requests=1)                              ;"""#240
<Response [422]>
"""
#_241=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 241 
_242=git.github_upload(f,print_requests=1)                              ;"""#242
<Response [422]>
"""
_243=f                                                                  ;"""#243
'/home/klk/test/fn/ '
"""
#get_ipython().run_line_magic('debug', 'git.github_upload(f,print_requests=1)')  # 244 
_245=T.path_legalized('//home/klk/test/fn/ ',reduce_space=False,)       ;"""#245
'/home/klk/test/fn/'
"""
#get_ipython().run_line_magic('debug', "T.path_legalized('//home/klk/test/fn/ ',reduce_space=False,)")  # 246 
_247=lambda : T.path_legalized('//home/klk/test/fn/ ',reduce_space=False,)  ;"""#247
<function __main__.<lambda>()>
"""
#get_ipython().run_line_magic('debug', '_247()')                        # 248 
#_249=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 249 
_250=git.github_upload(f,print_requests=1)                              ;"""#250
<Response [201]>
"""
_251=n                                                                  ;"""#251
364
"""
print(U.stime())
delta=n+1
for n,f in enumerate(fs[delta:]):
    n=n+delta
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):
        U.print_repr(r)
        continue
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 252 
_253=f                                                                  ;"""#253
'/home/klk/.local/lib/python3.6/site-packages/twisted/enterprise/adbapi.py'
"""
_254=git.github_upload(f,print_requests=1)                              ;"""#254
<Response [403]>
"""
print(_.json()['message'])                                              # 255 
_256=n                                                                  ;"""#256
9257
"""
_257=n,f                                                                ;"""#257
(9257,
 '/home/klk/.local/lib/python3.6/site-packages/twisted/enterprise/adbapi.py')
"""
_258=git.github_upload(f,print_requests=1)                              ;"""#258
<Response [201]>
"""
_259=n,f                                                                ;"""#259
(9257,
 '/home/klk/.local/lib/python3.6/site-packages/twisted/enterprise/adbapi.py')
"""
print(U.stime())
delta=n+1
for n,f in enumerate(fs[delta:]):
    n=n+delta
    U.p('%5s'%n+f[-11:])
    r=git.github_upload(f)
    if py.isno(r):
        U.print_repr(r)
        continue
    if r.status_code!=201:
        print(r)
        break
    
    #break                                                              # 260 
_261=len(fs)                                                            ;"""#261
11315
"""
#_262=ipy.save(_i260,out=1)                                             # 262 
_263=U.get_obj_file_lineno(_)                                           ;"""#263
("/home/klk/test/ipy/print(U.stime()) delta=n+1 for n,f in enumerate(fs[delta：])： n=n+delta U.p('%5s'%n+f[-11：]) r=git.github_upload(f) if py.isno(r)： U.print_repr(r) continue if r.status_code!=201： print(r) break #break.py",
 0)
"""
_264=U.get_obj_file_lineno(_)                                           ;"""#264
("/home/klk/test/ipy/print(U.stime()) delta=n+1 for n,f in enumerate(fs[delta：])： n=n+delta U.p('%5s'%n+f[-11：]) r=git.github_upload(f) if py.isno(r)： U.print_repr(r) continue if r.status_code!=201： print(r) break #break.py",
 0)
"""
f=U.get_obj_file_lineno(_)[0]                                           # 265 
#_266=ipy.save(_i260,out=1)                                             # 266 
_267=git.github_upload(f,print_requests=1)                              ;"""#267
<Response [201]>
"""
#get_ipython().run_line_magic('pinfo', 'F.replaceOnce')                 # 268 
#get_ipython().run_line_magic('pinfo2', 'F.replaceOnce')                # 269 
#_270=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 270 
_271=f                                                                  ;"""#271
"/home/klk/test/ipy/print(U.stime()) delta=n+1 for n,f in enumerate(fs[delta：])： n=n+delta U.p('%5s'%n+f[-11：]) r=git.github_upload(f) if py.isno(r)： U.print_repr(r) continue if r.status_code!=201： print(r) break #break.py"
"""
F.replace(f,'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','没必要吧')          # 272 
#_273=U.cdqp();
get_ipython().system('git pull origin master')
#U.cdb(p=1)
U.r(U,T,N,N.HTTP,F,py,git)
U.cdb()                                                                 # 273 
_274=F.replace(f,'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','没必要吧')     ;"""#274
"/home/klk/test/ipy/print(U.stime()) delta=n+1 for n,f in enumerate(fs[delta：])： n=n+delta U.p('%5s'%n+f[-11：]) r=git.github_upload(f) if py.isno(r)： U.print_repr(r) continue if r.status_code!=201： print(r) break #break.py"
"""
git.github_upload(f,print_requests==0)                                  # 275 
_276=git.github_upload(f,print_requests=0)                              ;"""#276
<Response [401]>
"""
print(_.json()['message'])                                              # 277 
_278=git.github_upload(f,print_requests=0)                              ;"""#278
<Response [401]>
"""
#get_ipython().run_line_magic('ll', '')                                 # 279 
_280=F.ls(U.pwd(),r=0,f=1)                                              ;"""#280
['/home/klk/.viminfo',
 '/home/klk/htop',
 '/home/klk/dstat',
 '/home/klk/.vimrc',
 '/home/klk/wsgi.py',
 '/home/klk/README.txt',
 '/home/klk/htop_1.0.2-3.dsc',
 '/home/klk/screenfetch-dev',
 '/home/klk/.profile',
 '/home/klk/.python_history',
 '/home/klk/.bashrc',
 '/home/klk/.pythonstartup.py',
 '/home/klk/.bash_history',
 '/home/klk/.gitconfig']
"""
_281=f                                                                  ;"""#281
"/home/klk/test/ipy/print(U.stime()) delta=n+1 for n,f in enumerate(fs[delta：])： n=n+delta U.p('%5s'%n+f[-11：]) r=git.github_upload(f) if py.isno(r)： U.print_repr(r) continue if r.status_code!=201： print(r) break #break.py"
"""
f=_280[0]                                                               # 282 
_283=git.github_upload(f,print_requests=1)                              ;"""#283
<Response [401]>
"""
#get_ipython().run_line_magic('cd', '/')                                # 284 
_285=F.ls(U.pwd(),r=0,f=1)                                              ;"""#285
['//.dockerenv']
"""
f=_[0]                                                                  # 286 
_287=git.github_upload(f,print_requests=1)                              ;"""#287
<Response [401]>
"""
_288=U.input_and_set('repo,token',default='',type=py.eval)              ;"""#288
('qgbcs/kp', '没必要吧')
"""
#ipy.save(_i260,out=1)                                                  # 289 
