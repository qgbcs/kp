# from qgb import U,T,N,F
# U.set_gst(U.pwd()+'test')
# from qgb.N.mirror_cache import app as application
# from flask_socketio import SocketIO
from socketio import Middleware


from pyxtermjs.app import app 
application=app
app.config["cmd"] = 'bash'
application=Middleware(None,app)

from gevent.pywsgi import WSGIServer

http_server = WSGIServer(('0.0.0.0', 8080), application)
http_server.serve_forever()


# from tornado.wsgi import WSGIContainer
# from tornado.httpserver import HTTPServer
# from tornado.ioloop import IOLoop
# import logging

# if __name__ == '__main__':
	# logging.basicConfig(level=logging.INFO)
	# HOST = '0.0.0.0'
	# http_server = HTTPServer(WSGIContainer(application))
	# http_server.listen(8080)
	# IOLoop.instance().start()
