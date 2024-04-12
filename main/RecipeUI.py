from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect


class RecipeUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recipe Finder")
        self.setGeometry(0, 0, 1090, 850)
        self.setStyleSheet("background-color: rgb(236, 235, 237);")

        central_widget = QWidget()
        central_widget.setGeometry(0, 0, 1090, 850)
        self.setCentralWidget(central_widget)

    def setup_ui(self):
        pass

    def setup_window(self):
        pass

    def layout_ui(self, recipes):
        pass

    def next(self):
        pass

    def previous(self):
        pass

    def first(self):
        pass

    def last(self):
        pass

    def search(self, recipe_keywords):
        pass

    def reset(self):
        pass
