import cv2
import face_recognition as fr
from time import sleep
import numpy as np
import progressbar


def main():
#Purpose : To blur out faces in a video stream to maintain privacy. This fucntion can be applied over any other project.
#Author  : Santosh D Kolur
    count=0            #count frame number
    copy_flocation=[]  #To maintain a copy of face_locations later.
    t=0                #To store time later
    
    video=input("Enter the name of the video file: Ex- Endgame.mp4 : ")
    image=fr.load_image_file(input("Enter the name of the file containing the face to be blurred including the extension.Ex: robert.jpg\n(If the image has more than one face both of them will be blurred out in the video)"))
    face_locations=fr.face_locations(image)
    img_face_encodings=fr.face_encodings(image,face_locations)
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    cap=cv2.VideoCapture(video)                               #Video capture through webcam. This could be changed to any video stream or a video file.
    ret,frame=cap.read()  
    out = cv2.VideoWriter("Output2.avi", cv2.VideoWriter_fourcc(*"XVID"), cap.get(cv2.CAP_PROP_FPS),(640,480))
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    bar = progressbar.ProgressBar(maxval=length,widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    while cap.isOpened():
        ret,frame=cap.read()                              #Read frame from webcam
        
        if ret == True:
            count=count+1
            bar.update(count+1)
            frame1=frame[:, :, ::-1]                                    #Converting BGR to RGB for face_recognition to work.
            face_locations=fr.face_locations(frame1)
            face_encodings=fr.face_encodings(frame,face_locations)
            for j,face_encoding in enumerate(face_encodings):
                result=fr.compare_faces(img_face_encodings,face_encoding)
                if( 1 in result ):       # If face found in the frame
                    f=face_locations[j]
                    top, right, bottom, left = f[0],f[1],f[2],f[3]
                    copy_flocation=face_locations
                    face =frame[top:bottom, left:right]
                    face = cv2.medianBlur(face,35,5)
                    face = cv2.GaussianBlur(face,(35,5),100)
                    frame[top:bottom, left:right]=face
            frame=cv2.resize(frame,(640,480))
            out.write(np.array(frame).astype('uint8'))
            #if(count==100):
                #break
                
                
            if cv2.waitKey(1) & 0xFF == ord('q'):                  #Press Q to close the window
                    break
            if count == length:
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()         
    bar.finish()


main()



