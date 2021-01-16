# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PersonFrm import Ui_FrmPerson


class Ui_Form(object):
    def OpenPersonWindow(self):
        self.frmperson = QMainWindow()
        self.uiPerson = Ui_FrmPerson()
        self.uiPerson.setupUi(self.frmperson)
        self.frmperson.show()
        

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")

        Form.resize(1008, 588)
        self.control_bt = QPushButton(Form)
        self.control_bt.setObjectName(u"control_bt")
        self.control_bt.setGeometry(QRect(97, 550, 72, 23))
        self.VideoBox = QGroupBox(Form)
        self.VideoBox.setObjectName(u"VideoBox")
        self.VideoBox.setGeometry(QRect(10, 40, 601, 481))
        self.image_label = QLabel(self.VideoBox)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(0, 20, 601, 461))
        self.BtnExit = QPushButton(Form)
        self.BtnExit.setObjectName(u"BtnExit")
        self.BtnExit.setGeometry(QRect(20, 550, 72, 23))
        self.LblTime = QLabel(Form)
        self.LblTime.setObjectName(u"LblTime")
        self.LblTime.setGeometry(QRect(890, 0, 111, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.LblTime.sizePolicy().hasHeightForWidth())
        self.LblTime.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.LblTime.setFont(font)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(620, 48, 381, 331))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 379, 329))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tableView = QTableWidget(Form)
        if (self.tableView.columnCount() < 4):
            self.tableView.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(620, 386, 381, 131))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.tableView.setFont(font1)
        self.ChBoxFaceDetect = QCheckBox(Form)
        self.ChBoxFaceDetect.setObjectName(u"ChBoxFaceDetect")
        self.ChBoxFaceDetect.setEnabled(True)
        self.ChBoxFaceDetect.setGeometry(QRect(264, 552, 92, 20))
        font2 = QFont()
        font2.setFamily(u"Microsoft Sans Serif")
        font2.setPointSize(10)
        self.ChBoxFaceDetect.setFont(font2)
        self.ChBoxFaceDetect.setTabletTracking(False)
        self.ChBoxFaceDetect.setLayoutDirection(Qt.RightToLeft)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(370, 530, 231, 51))
        self.groupBox.setLayoutDirection(Qt.RightToLeft)
        self.cnn = QRadioButton(self.groupBox)
        self.cnn.setObjectName(u"cnn")
        self.cnn.setGeometry(QRect(0, 20, 111, 21))
        self.hog = QRadioButton(self.groupBox)
        self.hog.setObjectName(u"hog")
        self.hog.setGeometry(QRect(120, 20, 91, 17))
        self.hog.setChecked(True)
        self.BtnPersons = QPushButton(Form)
        self.BtnPersons.setObjectName(u"BtnPersons")
        self.BtnPersons.setGeometry(QRect(620, 550, 71, 23))
        self.BtnPersons.clicked.connect(self.OpenPersonWindow)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Face detection", None))
        self.control_bt.setText(QCoreApplication.translate("Form", u"\u0634\u0631\u0648\u0639", None))
        self.VideoBox.setTitle(QCoreApplication.translate("Form", u"Camera", None))
        self.image_label.setText("")
        self.BtnExit.setText(QCoreApplication.translate("Form", u"\u062e\u0631\u0648\u062c", None))
        self.LblTime.setText(QCoreApplication.translate("Form", u"00:00:00", None))
        ___qtablewidgetitem = self.tableView.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u06a9\u062f \u0648\u0631\u0648\u062f", None));
        ___qtablewidgetitem1 = self.tableView.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u062a\u0627\u0631\u06cc\u062e", None));
        ___qtablewidgetitem2 = self.tableView.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0632\u0645\u0627\u0646", None));
        ___qtablewidgetitem3 = self.tableView.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u0646\u0627\u0645 \u0648 \u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc", None));
        self.ChBoxFaceDetect.setText(QCoreApplication.translate("Form", u"\u062a\u0634\u062e\u06cc\u0635 \u0686\u0647\u0631\u0647", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u062f\u0642\u062a \u062a\u0634\u062e\u06cc\u0635", None))
        self.cnn.setText(QCoreApplication.translate("Form", u"(CNN) \u062f\u0642\u062a \u0632\u06cc\u0627\u062f", None))
        self.hog.setText(QCoreApplication.translate("Form", u"(HOG) \u062f\u0642\u062a \u06a9\u0645", None))
        self.BtnPersons.setText(QCoreApplication.translate("Form", u"\u0627\u0634\u062e\u0627\u0635", None))
    # retranslateUi

