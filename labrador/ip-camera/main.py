from flask import Flask, render_template, Response
from camera import VideoCamera
import json

app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame_bytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video')
def video():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/image')
def image():
    return json.dumps({"image_base64": VideoCamera().get_frame_base64()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030, debug=True)