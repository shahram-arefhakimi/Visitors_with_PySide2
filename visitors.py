import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
import qimage2ndarray

from MainWindow import *

import face_recognition
import cv2

import time

height = 480
width = 640
channel = 3
step = channel * width
MODEL = "hog"

class MainWindow(QWidget):
    def __init__(self):
    
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.lastFrame=[]
        self.lastencode=[]
        self.lastlocations=[]
                
        # create a timer for clock
        self.timerClock = QTimer() 
        self.timerClock.timeout.connect(self.showTime) 
        self.timerClock.start(1000)
        # create exit button
        self.ui.BtnExit.clicked.connect(self.close_app)
        self.face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt.xml')
        if self.face_cascade.empty():
            QMessageBox.information(self, "Error Loading cascade classifier" , "Unable to load the face	cascade classifier xml file")
            sys.exit()

        # load video 
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.ShowVideos)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)
        self.ui.BtnExit.clicked.connect(self.close_app)
        
        

        #show clock top right
    def showTime(self): 
        current_time = QTime.currentTime() 
        label_time = current_time.toString('hh:mm:ss') 
        self.ui.LblTime.setText(label_time)


    def close_app(self):
        sys.exit(app.exec_())
        

        # start/stop timer
    def controlTimer(self):
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
            self.ui.control_bt.setText("توقف")
        else:
            self.timer.stop()
            self.cap.release()
            self.ui.control_bt.setText("شروع")


        # show video
    def ShowVideos(self):
        ret, frame = self.cap.read()
       # call facedetection
        if self.ui.ChBoxFaceDetect.isChecked():
            self.FaceDetected(frame)
        # resize frame image
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        self.ui.image_label.setPixmap(QPixmap.fromImage(image))    

        # Faces Detected
    def FaceDetected(self,frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_rects = self.face_cascade.detectMultiScale(gray, 1.3, 5)    
        for (x, y, w, h) in face_rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # locations = face_recognition.face_locations(frame, model=MODEL)
        # Frame_encodes= face_recognition.face_encodings(frame,locations)
        # now_faces=zip(Frame_encodes,locations)
        # if (self.CompareLastFrames(now_faces,self.lastencode)):
        #     pass
        #     #for all detected faces
        # else:
        #     self.lastencode = Frame_encodes
        # for (y1, x2, y2, x1) in locations:
        #     cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
