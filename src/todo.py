# Todo App

import sys
from typing import List,Tuple, Optional

# Modified Imports
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QAbstractListModel, Qt, QModelIndex

# Import UI
from TodoMainWindow import Ui_todoMainWindow

# This is the Model. Can this be imported from a standalone file. 
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


# What is this Main Window? Is this the View/Controller(?) and connects the Model with View/Controller(?)
# Or is this MainWindow class a "Delegator"?  
class MainWindow(QMainWindow, Ui_todoMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel(todos = [(False,"Minstrone Soup"),(False,"Chicken Parmesan")])
        # self.model = TodoModel()
        self.todoView.setModel(self.model)
        # Connect add button signal to add_item action. 
        self.addButton.clicked.connect(self.add_item)
        self.deleteButton.clicked.connect(self.delete_item)
        self.completeButton.clicked.connect(self.complete_item)

    def add_item(self) -> None:
        """
        Get item from todoEdit, add to todos, then clear it.  
        """
        # Get text entered in box
        item_text = self.todoEdit.text()
        item_status = False
        # Add to memory
        if item_text:
            self.model.todos.append((item_status,item_text))
            # Emit signal from model that shape of list i.e. layout has changed. This causes QListView to redraw. 
            self.model.layoutChanged.emit()
            # Clear text entered in box
            self.todoEdit.clear()


            # Debug print. 
            print(self.model.todos[-1])

    def delete_item(self) -> None:
        """
        Delete user selected item from todos, reflect it in list. 
        """
        # Get index of items selected by user. 
        user_sel = self.todoView.selectedIndexes()
        # If no selections are active, do nothing. 
        if user_sel:
            user_sel_idx = user_sel[0].row()
            # Delete data from storage list
            self.model.todos.pop(user_sel_idx)
            # Refresh view. 
            self.model.layoutChanged.emit()
            # Clear selection because index selected could be out of bounds...
            # and a new selection from user is encouraged.  
            self.todoView.clearSelection()


    def complete_item(self) -> None: 
        """
        Mark user selected item as complete. 
        """
        # Get index of items selected by user. 
        user_sel = self.todoView.selectedIndexes()
        # If no selections are active, do nothing. 
        if user_sel:
            user_sel_idx = user_sel[0].row()
            user_sel_item = self.model.todos[user_sel_idx]
            user_sel_item_str = user_sel_item[1]
            new_item = (True,user_sel_item_str)
            # Delete old item and replace with new item
            self.model.todos.pop(user_sel_idx)
            self.model.todos.insert(user_sel_idx,new_item)
            # Refresh view. 
            self.model.layoutChanged.emit()
            # Clear selection 
            self.todoView.clearSelection()

            # Debug print. 
            print(self.model.todos[user_sel_idx])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()