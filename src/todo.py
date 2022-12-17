# Todo App

import sys
from typing import List,Tuple, Optional

# Modified Imports
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QAbstractListModel, Qt, QModelIndex

# Import UI
from TodoMainWindow import Ui_todoMainWindow

# This is the Model
class TodoModel(QAbstractListModel):
    def __init__(self, todos: Optional[List[Tuple[bool,str]]] = None) -> None:
        super().__init__()
        self.todos = todos or []  # Data store. 
    
    # Handles requests for data from the view and returns appropriate result. 
    def data(self, index: QModelIndex, role: Qt.DisplayRole) -> str:
        "Return data for index row as requested by role."
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text

    def rowCount(self,index: QModelIndex) -> int:
        # Get number of rows in current data.  
        return len(self.todos)


# Main Window is the View/Controller(?) and connects the Model with View/Controller(?) 
class MainWindow(QMainWindow, Ui_todoMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel(todos = [(False,"Minstrone Soup"),(False,"Chicken Parmesan")])
        self.todoView.setModel(self.model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
