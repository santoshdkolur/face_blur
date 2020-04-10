# Face Blur
This is a simple project which blurs out the faces to hide the person's identity.
Blurs out faces in a video stream to maintain privacy. This fucntion can be applied over any other project.
The code is written using opencv and face_recognition libraries. Python 3.7 is used to code the project.

The repo contains two files which basically have the same code. One is the python notebook file (.ipynb) and another python(.py) file.
You can run the py file normally as you would for any python script.

face_blur blurs the faces in the live video stream. 

face_blur_allFaces blurs out all the faces in the video. Input: Name of the video file
![](all_blur.gif)

face_blue_selectedFace blurs out only the faces that are present in the video that are in the input image. Input name of the video file and the name of the image

![](robert_blur.gif)

If you want to increase the frames processed per second or if you face any increase in time to process the frames when you applied it over your project, you can always build opencv to run on your gpu. 

##### Note : opencv does not run on gpu by default. You'll have to build one to run on your gpu from source. Refer the following link: https://jamesbowley.co.uk/build-opencv-4-0-0-with-cuda-10-0-and-intel-mkl-tbb-in-windows/
