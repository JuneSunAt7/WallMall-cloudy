# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WallMall-cloudy/methods/keys.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormKeys(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(893, 499)
        Form.setStyleSheet("border: 2px solid #434965;\n"
"border-radius: 7px;\n"
"background-color: #2A2F41;")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.radioButton = QtWidgets.QRadioButton(self.splitter)
        self.radioButton.setMinimumSize(QtCore.QSize(0, 40))
        self.radioButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.splitter)
        self.radioButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.splitter)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(0, 350))
        self.frame.setStyleSheet("background-color: #2A2F41;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton.setStyleSheet("QPushButton{\n"
" color: white;\n"
"border-radius: 7px;\n"
"background-color: #595F76;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #50566E;\n"
"}\n"
"QPushButton:pressed{\n"
" background-color: #434965;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
" color: white;\n"
"border-radius: 7px;\n"
"background-color: #595F76;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #50566E;\n"
"}\n"
"QPushButton:pressed{\n"
" background-color: #434965;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.splitter_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ключи"))
        self.radioButton.setText(_translate("Form", "Пароль"))
        self.radioButton_2.setText(_translate("Form", "Внешний ЭК"))
        self.pushButton.setText(_translate("Form", "Отменить"))
        self.pushButton_2.setText(_translate("Form", "Сохранить "))
