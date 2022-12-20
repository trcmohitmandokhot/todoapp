# Todo App
import os
import json
import sys

# Import PyQt5 Application Instance and MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

# Import UI
from ui.TodoMainWindow import Ui_todoMainWindow

# Import Model from submodule
from models.todo import TodoModel

DATA_DIR = "/home/devel/code/qtgui/todoapp/todo/data"

# MainWindow has all of the core stiching logic between model and view. 
class MainWindow(QMainWindow, Ui_todoMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        # self.model = TodoModel(todos = [(False,"Minstrone Soup"),(False,"Chicken Parmesan")])
        self.model = TodoModel()
        self.load()
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
            self.save()

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
            self.save()

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
            self.save()

    def load(self):
        try:
            with open(os.path.join(DATA_DIR,"user1.json"),"r") as f:
                self.model.todos = json.load(f)
        except FileNotFoundError as e:
            print(e)
        except json.JSONDecodeError as e:
            if os.stat(f).st_size == 0: 
                print("Empty database")
            else:
                print(e)

    def save(self):
        try:
            with open(os.path.join(DATA_DIR,"user1.json"),"w") as f:
                data = json.dump(self.model.todos,f)
        except FileNotFoundError as e:
            print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
