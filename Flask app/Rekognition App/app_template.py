from flask import Flask, render_template, Response, redirect
import cv2, boto3
from VideoCamera import VideoCamera
from dotenv import load_dotenv

app = Flask(__name__)
videoStream = VideoCamera() #instantiate a VideoCamera() class from my imported modules

curr_detection_mode = 0
#three different modes:
#0 = detect faces (default)
#1 = detect labels
#2 = detect texts

# -------------------------------------------
#decorate routes

#default route
@app.route('/')
def reroute():
    return redirect('/main')

@app.route('/main')
def mainPage():
    return render_template("/Frontend/home.html")


#create routes for Camera, Detect faces, Detect labels, Detect texts
@app.route('/camera')
def cameraPage():
    return render_template('/Frontend/camera.html')

#generator function for the camera
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n\r\n') #b -> byte strings


#use the VideoCamera() object videoStream to generate/send images
@app.route('/video_feed')
def video_feed():
    return Response(gen(videoStream), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/detect_faces')
def detect_faces():
    global curr_detection_mode
    curr_detection_mode = 0

    return render_template('/Frontend/output.html')

@app.route('/detect_labels')
def detect_labels():
    global curr_detection_mode
    curr_detection_mode = 1

    return render_template('/Frontend/output.html')

@app.route('/detect_texts')
def detect_texts():
    global curr_detection_mode
    curr_detection_mode = 2

    return render_template('/Frontend/output.html')

@app.route('/source_image')
#sending the image to be rendered
def source_image():
    global curr_detection_mode
    if curr_detection_mode == 0:
        #detect faces
        picture = videoStream.face_detections()
    elif curr_detection_mode == 1:
        #detect labels
        picture = videoStream.label_detections()
    else:
        #detect texts
        picture = videoStream.text_detections()

    return picture



if __name__ == "__main__":
    app.run()