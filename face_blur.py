import cv2
import face_recognition as fr
import datetime

def main():
#Purpose : To blur out faces in a video stream to maintain privacy. This fucntion can be applied over any other project.
#Author  : Santosh D Kolur

    copy_flocation=[]  #To maintain a copy of face_locations later.
    t=0                #To store time later
    video_capture=cv2.VideoCapture(0)                               #Video capture through webcam. This could be changed to any video stream or a video file.
    while True:
        ret,frame=video_capture.read()                              #Read frame from webcam
        frame1=frame[:, :, ::-1]                                    #Converting BGR to RGB for face_recognition to work.
        face_locations=fr.face_locations(frame1)
        if(len(face_locations)>0):                                  #Fix a faulty frame i.e. if face is not detected in a certain frame due to movement
            t=datetime.datetime.now()
        elif t!=0:                                                  #Sometime opencv returns nonetype frame in the beginnig
            t2=datetime.datetime.now()
            t3=t2-t
            if t3.seconds <= 1 and t3.microseconds > 0:
                   for (top, right, bottom, left) in copy_flocation: 
                        #Blur the same area where the face was previously detected for a second.
                        #Helps when using in low light
                        copy_flocation=face_locations
                        face = frame[top:bottom, left:right]
                        face = cv2.medianBlur(face,35,5)
                        face = cv2.GaussianBlur(face,(35,5),100)
                        frame[top:bottom, left:right]=face
            if cv2.waitKey(1) & 0xFF == ord('q'):                  #Press Q to close the window
                break

        for (top, right, bottom, left) in face_locations:      
            copy_flocation=face_locations
            face = frame[top:bottom, left:right]
            face = cv2.medianBlur(face,35,5)                    #Applying MedianBlur to reduce features
            face = cv2.GaussianBlur(face,(35,5),100)            #GaussianBlur blurs out the face even more
            frame[top:bottom, left:right]=face
            # Draw a box around the face
            #cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.imshow('Video',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()

main()
