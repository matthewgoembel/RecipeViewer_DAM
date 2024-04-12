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

    def setup_window(self):
        # Set up window dimensions, title, etc.
        pass

    def layout_ui(self, recipes):
        # Layout recipes in the UI using QGridLayout
        pass

    def next(self):
        # Display next set of recipes
        pass

    def previous(self):
        # Display previous set of recipes
        pass

    def first(self):
        # Jump to beginning of recipe list
        pass

    def last(self):
        # Jump to end of recipe list
        pass

    def search(self, recipe_keywords):
        # Search for recipes containing keywords
        pass

    def reset(self):
        # Clear search results and return to normal pagination
        pass
