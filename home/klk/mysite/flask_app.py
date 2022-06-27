
# A very simple Flask Hello World app for you to get started with...
from qgb import *
from flask import Flask
app = Flask(__name__)
app.debug=True

# print(U.dir(N))

t,app2=N.rpcServer(app=app,locals=globals(),globals=globals())
#U.id(app,app2) # Equal

# from flask import request

# import sys,os
# import traceback as tb

# @app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    #raise Exception(2333)
    return T.az
    return str([233,T,request.headers,U])
    #r=tb.extract_tb( sys.last_traceback)
    #r.append(sys.last_value)
    #return 'Hello from Flask!'
    return str(dict(os.environ))
    return str(sys.path)+str([2333333,sys.modules,123])


