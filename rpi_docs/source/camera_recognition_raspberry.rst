Camera Recognition
====================

In this project, we will make a color recognizer, connect a camera module to the Raspberry Pi, use ``PiCamera`` and ``OpenCV`` to process the objects captured by the camera, and express its colors with RGB Matrix HAT.

.. note::
    This example needs to enable the Raspberry Pi `Camera function <https://docs.sunfounder.com/projects/raphael-kit/en/latest/components/component_camera_module.html#camera-module>`_.

    Then install third-party dependencies

    .. raw:: html

        <run></run>

    .. code-block::

        sudo pip3 install opencv-contrib-python
        sudo apt-get install -y python3-h5py libatlas-base-dev
        sudo pip3 install -U numpy


**Run the code**

When the program is running, hold the camera moduel and aim at some brightly colored objects, you will find that the RGB Matrix HAT also shows similar colors.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/rgb_matrix/raspberrypi
    sudo python3 camera.py  

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``rgb_matrix/raspberrypi``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    # To run this example, you need to turn on Camera on raspi-config => Interfacing => Camera
    # Then run the following command to install dependencies
    # sudo pip3 install opencv-contrib-python
    # sudo apt-get install -y python3-h5py libatlas-base-dev
    # sudo pip3 install -U numpy

    from picamera.array import PiRGBArray # Generates a 3D RGB array
    from picamera import PiCamera
    import time
    import cv2

    from PIL import Image
    from rgb_matrix import RGB_Matrix

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

**How it works?**

.. code-block:: python

    from picamera.array import PiRGBArray # Generates a 3D RGB array
    from picamera import PiCamera
    import time
    import cv2

    from PIL import Image
    from rgb_matrix import RGB_Matrix

* Import ``PiCamera`` to support the use of the camera.
* Import ``PiRGBArray`` to help the Raspberry Pi output the captured images in the form of an array.
* Import ``OpenCV`` vision library where ``cv2``` is the name of the C++ namespace of Opencv.
* Import the image processing library ``PIL`` of the python platform.

.. code-block:: python

    camera = PiCamera()
    camera.resolution = (1280, 720)raw_capture = PiRGBArray(camera, size=(1280, 720))

Create a ``PiCamera`` object and call ``PiRGBArray()`` to generate an RGB three-dimensional array with a resolution of (1280, 720) and pass it to ``raw_capture``.

.. code-block:: python

    for frame in camera.capture_continuous(raw_capture, format="rgb", use_video_port=True):
        
        image = frame.array

Traverse the images captured by the camera and pass them to the image in the form of an RGB three-dimensional array.

.. code-block:: python

    img = cv2.resize(image, (8, 8), interpolation = cv2.INTER_AREA)
    im_pil = Image.fromarray(img)

Convert the picture into an 8x8 RGB Matrix HAT and pass it to ``im_pil`` in the form of an array.

.. code-block:: python

    rr.image(list(im_pil.getdata()))

Convert ``im_pil`` into a list form to be used as a parameter of ``rr.image`` to light up the RGB Matrix HAT.

.. code-block:: python

    raw_capture.truncate(0)

Clear ``raw_capture`` in this loop.

