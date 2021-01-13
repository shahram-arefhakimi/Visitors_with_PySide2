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

        # load video 
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.detectFaces)
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
    def detectFaces(self):
        ret, frame = self.cap.read()
        # resize frame image
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        self.ui.image_label.setPixmap(QPixmap.fromImage(image))    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
