import sys;'qgb.U' in sys.modules or sys.path.append('C:/QGB/babun/cygwin/bin/');
from qgb import U,T,N,F,py

from threading import Lock
from flask import Flask, render_template, session, request,copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room,close_room, rooms, disconnect

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.jinja_loader.searchpath.append(U.pwd())
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

N.rpcServer(locals=globals(),globals=globals(),app=app,key='-')

def background_thread():
	"""Example of how to send server generated events to clients."""
	count = 0
	while True:
		socketio.sleep(10)
		count += 1
		socketio.emit('my_response',
					  {'data': 'Server generated event', 'count': count})



@app.route("/")
def index():
	return render_template("index.html")



@socketio.on('message')
def print_message(*a,**ka):
	## When we receive a new event of type
	## 'message' through a socket.io connection
	## we print the socket ID and the message
	print(request.sid,"len:%s "%U.len(a,ka) ,a,ka)
	emit('r', {'data': 'qgb print', 'count': 0})
	print('='*88)



import socket
socket._LOCALHOST='192.168.43.162'
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import logging

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	HOST = '0.0.0.0'
	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(8080)
	IOLoop.instance().start()



	
if __name__ == '__main__':
	# socketio.run(app,host='192.168.43.162',port=8080)
	application=app
	from gevent.pywsgi import WSGIServer
	http_server = WSGIServer(('0.0.0.0', 8080), application)
	http_server.serve_forever()