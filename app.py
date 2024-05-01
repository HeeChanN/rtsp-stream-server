from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import cv2
from base64 import b64encode
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def capture_frames(rtsp_url):
    cap = cv2.VideoCapture(rtsp_url)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        _, buffer = cv2.imencode('.jpg', frame)
        frame_data = b64encode(buffer).decode('utf-8')
        socketio.emit('frame', {'data': 'data:image/jpeg;base64,' + frame_data}, namespace='/video')
        time.sleep(0.1)  # Adjust the sleep time according to your frame rate requirements

@socketio.on('connect', namespace='/video')
def test_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/video')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    rtsp_url = 'rtsp://210.99.70.120:1935/live/cctv001.stream'
    from threading import Thread
    thread = Thread(target=capture_frames, args=(rtsp_url,))
    thread.start()
    socketio.run(app, host='0.0.0.0', port=5000)

