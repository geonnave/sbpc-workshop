import cv2
import base64

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame_jpeg(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg

    def get_frame_bytes(self):
        jpeg = self.get_frame_jpeg()
        return jpeg.tobytes()

    def get_frame_base64(self):
        jpeg = self.get_frame_jpeg()
        return base64.b64encode(jpeg).decode("utf-8")