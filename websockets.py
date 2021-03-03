from flask_socketio import emit
from flask import session


def websockets_with_app_and_socketio(app, socketio):
    @socketio.on('connect', namespace='/test')
    def test_connect():
        print("A user Connected")

    @socketio.on('my_event', namespace='/test')
    def test_message(message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        print("GOT MESSAGE TO SERVER : ", message['data'])
        emit('my_response',
             {'data': message['data'], 'count': session['receive_count']})
