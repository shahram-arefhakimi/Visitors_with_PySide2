# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'persons.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FrmPerson(object):
    def setupUi(self, FrmPerson):
        if not FrmPerson.objectName():
            FrmPerson.setObjectName(u"FrmPerson")
        FrmPerson.resize(522, 379)
        self.widget = QWidget(FrmPerson)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 340, 501, 41))
        self.BtnExit = QPushButton(self.widget)
        self.BtnExit.setObjectName(u"BtnExit")
        self.BtnExit.setGeometry(QRect(10, 10, 75, 23))
        self.BtnNew = QPushButton(self.widget)
        self.BtnNew.setObjectName(u"BtnNew")
        self.BtnNew.setGeometry(QRect(420, 10, 75, 23))
        self.BtnSave = QPushButton(self.widget)
        self.BtnSave.setObjectName(u"BtnSave")
        self.BtnSave.setGeometry(QRect(340, 10, 75, 23))
        self.BtnEdit = QPushButton(self.widget)
        self.BtnEdit.setObjectName(u"BtnEdit")
        self.BtnEdit.setGeometry(QRect(260, 10, 75, 23))
        self.LblImage = QLabel(FrmPerson)
        self.LblImage.setObjectName(u"LblImage")
        self.LblImage.setGeometry(QRect(10, 50, 261, 281))
        self.LblImage.setFrameShape(QFrame.Box)
        self.LblImage.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(FrmPerson)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(280, 50, 231, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textEdit_2 = QTextEdit(self.layoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.horizontalLayout_2.addWidget(self.textEdit_2)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamily(u"IRANSansWeb")
        self.label_4.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.tableWidget = QTableWidget(FrmPerson)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(280, 90, 231, 241))
        self.widget1 = QWidget(FrmPerson)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 501, 31))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.widget1)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.widget1)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout.addWidget(self.textEdit)

        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)


        self.retranslateUi(FrmPerson)

        QMetaObject.connectSlotsByName(FrmPerson)
    # setupUi

    def retranslateUi(self, FrmPerson):
        FrmPerson.setWindowTitle(QCoreApplication.translate("FrmPerson", u"Dialog", None))
        self.BtnExit.setText(QCoreApplication.translate("FrmPerson", u"\u062e\u0631\u0648\u062c", None))
        self.BtnNew.setText(QCoreApplication.translate("FrmPerson", u"\u062c\u062f\u06cc\u062f", None))
        self.BtnSave.setText(QCoreApplication.translate("FrmPerson", u"\u0630\u062e\u06cc\u0631\u0647", None))
        self.BtnEdit.setText(QCoreApplication.translate("FrmPerson", u"\u062d\u0630\u0641", None))
        self.LblImage.setText(QCoreApplication.translate("FrmPerson", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("FrmPerson", u"\u0648\u0632\u0646 :", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FrmPerson", u"\u0646\u0627\u0645", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FrmPerson", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FrmPerson", u"\u0648\u0632\u0646", None));
        self.label_2.setText(QCoreApplication.translate("FrmPerson", u"\u0646\u0627\u0645 \u062e\u0627\u0646\u0648\u0627\u062f\u06af\u06cc :", None))
        self.label.setText(QCoreApplication.translate("FrmPerson", u"\u0646\u0627\u0645 :", None))
    # retranslateUi


if __name__== "__main__" :
    import sys
    PersonWindow=QMainWindow()
    ui=Ui_Form()
    ui.setupUi(PersonWindow)
    PersonWindow.show()
    sys.exit(app.exec_())