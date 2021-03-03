from websockets import websockets_with_app_and_socketio
from routes import routes_with_app
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from sql_helper import DB
from threading import Lock
from flask_cors import CORS

async_mode = None
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None
thread_lock = Lock()
data = DB({"HOST": "localhost", "USER": "root",
           "PASSWORD": "jayvishaal", "DB": "test"}, socketio)
routes_with_app(app, data)
websockets_with_app_and_socketio(app, socketio)

if __name__ == '__main__':
    app.run(debug=True)
