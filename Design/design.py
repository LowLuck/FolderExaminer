# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design\MainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BigFolderFounder(object):
    def setupUi(self, BigFolderFounder):
        BigFolderFounder.setObjectName("FolderExaminer")
        BigFolderFounder.resize(393, 491)
        self.lineEdit = QtWidgets.QLineEdit(BigFolderFounder)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 221, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(BigFolderFounder)
        self.label.setGeometry(QtCore.QRect(10, 11, 51, 20))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(BigFolderFounder)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 371, 441))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(BigFolderFounder)
        self.pushButton.setGeometry(QtCore.QRect(300, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(BigFolderFounder)
        QtCore.QMetaObject.connectSlotsByName(BigFolderFounder)

    def retranslateUi(self, BigFolderFounder):
        _translate = QtCore.QCoreApplication.translate
        BigFolderFounder.setWindowTitle(_translate("FolderExaminer", "FolderExaminer"))
        self.label.setText(_translate("FolderExaminer", "Path to folder"))
        self.pushButton.setText(_translate("FolderExaminer", "Input"))
