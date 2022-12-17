import sys

# Original Imports
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import Qt

# Modified Imports
from PyQt5.QtWidgets import QApplication, QMainWindow


from TodoMainWindow import Ui_todoMainWindow

# Multiple Inheritance(Why?) - QtDesigner generated .ui uses MainWindow functions, that need referenced. 
class MainWindow(QMainWindow, Ui_todoMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
