import sys
import os

# Original Imports
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import Qt

# Modified Imports
from PyQt5.QtWidgets import QApplication, QMainWindow


from PyQt5 import uic

basedir = os.path.dirname(__file__)

# Load from UIC
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(basedir,'todomainwindow.ui'),self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
