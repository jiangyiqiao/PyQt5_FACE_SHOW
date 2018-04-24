# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(693, 462)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/timg.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton_open = QtWidgets.QPushButton(Dialog)
        self.pushButton_open.setGeometry(QtCore.QRect(590, 410, 70, 30))
        self.pushButton_open.setObjectName("pushButton_open")
        self.label_input = QtWidgets.QLabel(Dialog)
        self.label_input.setGeometry(QtCore.QRect(10, 70, 310, 310))
        self.label_input.setText("")
        self.label_input.setObjectName("label_input")
        self.label_result = QtWidgets.QLabel(Dialog)
        self.label_result.setGeometry(QtCore.QRect(10, 410, 511, 30))
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.label_output = QtWidgets.QLabel(Dialog)
        self.label_output.setGeometry(QtCore.QRect(339, 70, 341, 310))
        self.label_output.setText("")
        self.label_output.setObjectName("label_output")
        self.lineEdit_url = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_url.setGeometry(QtCore.QRect(130, 10, 331, 30))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 91, 30))
        self.label_4.setObjectName("label_4")
        self.pushButton_recog = QtWidgets.QPushButton(Dialog)
        self.pushButton_recog.setGeometry(QtCore.QRect(490, 10, 70, 30))
        self.pushButton_recog.setObjectName("pushButton_recog")

        self.retranslateUi(Dialog)
        self.pushButton_open.clicked.connect(Dialog.openImage)
        self.pushButton_recog.clicked.connect(Dialog.recognise)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FACE RECOGNISE"))
        self.pushButton_open.setText(_translate("Dialog", "打开图片"))
        self.label_4.setText(_translate("Dialog", "输入图像url: "))
        self.pushButton_recog.setText(_translate("Dialog", "识别"))

