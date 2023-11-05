# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todomainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_todoMainWindow(object):
    def setupUi(self, todoMainWindow):
        todoMainWindow.setObjectName("todoMainWindow")
        todoMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(todoMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(40, 370, 281, 61))
        self.deleteButton.setObjectName("deleteButton")
        self.completeButton = QtWidgets.QPushButton(self.centralwidget)
        self.completeButton.setGeometry(QtCore.QRect(470, 370, 281, 61))
        self.completeButton.setObjectName("completeButton")
        self.todoView = QtWidgets.QListView(self.centralwidget)
        self.todoView.setGeometry(QtCore.QRect(40, 30, 711, 311))
        self.todoView.setObjectName("todoView")
        self.todoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.todoEdit.setGeometry(QtCore.QRect(40, 450, 711, 51))
        self.todoEdit.setObjectName("todoEdit")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(40, 520, 711, 61))
        self.addButton.setObjectName("addButton")
        todoMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(todoMainWindow)
        QtCore.QMetaObject.connectSlotsByName(todoMainWindow)

    def retranslateUi(self, todoMainWindow):
        _translate = QtCore.QCoreApplication.translate
        todoMainWindow.setWindowTitle(_translate("todoMainWindow", "MainWindow"))
        self.deleteButton.setText(_translate("todoMainWindow", "Delete"))
        self.completeButton.setText(_translate("todoMainWindow", "Complete"))
        self.addButton.setText(_translate("todoMainWindow", "Add Todo"))
