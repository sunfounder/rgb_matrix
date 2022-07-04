# To run this example, youneed to turn on Camera on raspi-config => Interfacing => Camera
# Then run the following command to install dependencies
# sudo apt update
# sudo apt install -y python3-opencv 
# sudo apt-get install -y python3-h5py libatlas-base-dev
# sudo pip3 install -U numpy

from picamera.array import PiRGBArray # Generates a 3D RGB array
from picamera import PiCamera
import time
import cv2

from PIL import Image
from rgb_matrix.rgb_matrix import RGB_Matrix

rr = RGB_Matrix(0X74)

camera = PiCamera()
camera.resolution = (1280, 720)
raw_capture = PiRGBArray(camera, size=(1280, 720))
# Allow the camera to warmup
time.sleep(0.1)
# Grab an image from the camera
for frame in camera.capture_continuous(raw_capture, format="rgb", use_video_port=True):
     
    image = frame.array

    # Convert image to 8x8 for RGB matrix
    img = cv2.resize(image, (8, 8), interpolation = cv2.INTER_AREA)
    im_pil = Image.fromarray(img)

    # Render
    rr.image(list(im_pil.getdata()))

    raw_capture.truncate(0)