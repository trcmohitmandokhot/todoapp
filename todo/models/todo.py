from PyQt5.QtCore import QAbstractListModel, Qt, QModelIndex
from PyQt5.QtGui import QColor
from typing import List, Tuple, Optional

COLOR_GREEN = QColor("green")
COLOR_RED = QColor("red")

# This is the Model. Can this be imported from a standalone file.


class TodoModel(QAbstractListModel):
    def __init__(self, todos: Optional[List[Tuple[bool, str]]] = None) -> None:
        super().__init__()
        self.todos = todos or []  # Data store.

    # Handles requests for data from the view and returns appropriate result.
    def data(self, index: QModelIndex, role: Qt.DisplayRole) -> str:
        "Return data for index row as requested by role."
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text

        # Decorate color of text based on status.
        if role == Qt.DecorationRole:
            status, text = self.todos[index.row()]
            if status:
                return COLOR_GREEN
            else:
                return COLOR_RED

    def rowCount(self, index: QModelIndex) -> int:
        # Get number of rows in current data.
        return len(self.todos)
