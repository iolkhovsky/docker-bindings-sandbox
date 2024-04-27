import cv2
import requests
from flask import Flask, Response
import threading
import numpy as np

app = Flask(__name__)

frame_buffer = None
lock = threading.Lock()

def capture_and_send_frames():
    global frame_buffer
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        _, buffer = cv2.imencode('.jpg', frame)
        response = requests.post('http://localhost:55501/process', files={'image': buffer.tobytes()})
        
        if response.status_code == 200:
            nparr = np.frombuffer(response.content, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            with lock:
                frame_buffer = img_np.copy()

    cap.release()

def generate():
    global frame_buffer
    while True:
        with lock:
            if frame_buffer is not None:
                _, buffer = cv2.imencode('.jpg', frame_buffer)
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
        cv2.waitKey(1)

@app.route('/video_feed')
def video_feed():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    thread = threading.Thread(target=capture_and_send_frames)
    thread.start()
    app.run(host='0.0.0.0', port=55502, debug=True)
