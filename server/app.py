from flask import Flask, request, send_file, make_response
import cv2
import numpy as np
from io import BytesIO

import img_proc_lib as improc


app = Flask(__name__)


@app.route('/process', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return "No image file provided", 400

    file = request.files['image']
    image_stream = file.read()
    image = np.frombuffer(image_stream, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    result = improc.blur(image)

    is_success, buffer = cv2.imencode(".jpg", result)
    if not is_success:
        return "Could not encode image", 500

    return send_file(BytesIO(buffer), mimetype='image/jpeg')


@app.route('/')
def status():
    response = make_response('Ok, server is working', 200)
    response.mimetype = "text/plain"
    return response


if __name__ == '__main__':
    app.run(debug=True, port=55501, host='0.0.0.0')
