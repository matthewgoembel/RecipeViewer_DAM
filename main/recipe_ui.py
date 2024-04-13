import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, \
    QVBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout


class RecipeUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup the main window
        self.setup_window()
        # Setup the UI layout
        self.layout_ui()
        # Translate UI elements
        self.retranslate_ui()

    def setup_window(self):
        # Set properties for the main window
        self.setObjectName("main_window")
        self.resize(1090, 850)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                           "background-color: rgb(236, 235, 237);")

    def layout_ui(self):
        # Create central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create horizontal layout widget for search bar
        self.horizontal_layout_widget = QWidget(self.central_widget)
        self.horizontal_layout_widget.setGeometry(10, 10, 1061, 31)
        self.search_bar_layout = QHBoxLayout(self.horizontal_layout_widget)
        self.search_bar_layout.setContentsMargins(0, 0, 0, 0)

        # Create search line edit widget
        self.search_line = QLineEdit(self.horizontal_layout_widget)
        self.search_line.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Create search and reset buttons
        self.search_button = QPushButton("Search", self.horizontal_layout_widget)
        self.search_button.setMaximumSize(80, 20)
        self.reset_button = QPushButton("Reset", self.horizontal_layout_widget)
        self.reset_button.setMaximumSize(80, 20)

        # Add widgets to search bar layout
        self.search_bar_layout.addWidget(self.search_line)
        self.search_bar_layout.addWidget(self.search_button)
        self.search_bar_layout.addWidget(self.reset_button)

        # Create horizontal layout widget for navigation buttons
        self.horizontal_layout_widget_2 = QWidget(self.central_widget)
        self.horizontal_layout_widget_2.setGeometry(690, 780, 395, 30)
        self.page_button_layout = QHBoxLayout(self.horizontal_layout_widget_2)
        self.page_button_layout.setContentsMargins(0, 0, 0, 0)

        # Create navigation buttons
        self.prev_button = QPushButton("<< Previous", self.horizontal_layout_widget_2)
        self.prev_button.setMaximumSize(100, 20)
        self.first_button = QPushButton("First", self.horizontal_layout_widget_2)
        self.first_button.setMaximumSize(70, 20)
        self.last_button = QPushButton("Last", self.horizontal_layout_widget_2)
        self.last_button.setMaximumSize(60, 20)
        self.next_button = QPushButton("Next >>", self.horizontal_layout_widget_2)
        self.next_button.setMaximumSize(100, 20)

        # Add navigation buttons to layout
        self.page_button_layout.addWidget(self.prev_button)
        self.page_button_layout.addWidget(self.first_button)
        self.page_button_layout.addWidget(self.last_button)
        self.page_button_layout.addWidget(self.next_button)

        # Create label for displaying recipe count
        self.display_recipe_count_label = QLabel(self.central_widget)
        self.display_recipe_count_label.setGeometry(0, 820, 1091, 31)
        self.display_recipe_count_label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0.966, x2:0.995, y2:0.119773, stop:0 rgba(134, "
            "134, 134, 255), stop:1 rgba(234, 234, 234, 255));")
        self.display_recipe_count_label.setFrameShape(QLabel.Box)
        self.display_recipe_count_label.setFrameShadow(QLabel.Plain)

        # Create grid layout for recipes
        self.grid_layout_widget = QWidget(self.central_widget)
        self.grid_layout_widget.setGeometry(10, 50, 1071, 721)
        self.recipe_grid_layout = QGridLayout(self.grid_layout_widget)
        self.recipe_grid_layout.setContentsMargins(0, 0, 0, 0)

    def retranslate_ui(self):
        # Translate UI labels and button text
        self.setWindowTitle("Recipe Viewer")
        self.prev_button.setText("<< Previous")
        self.first_button.setText("First")
        self.last_button.setText("Last")
        self.next_button.setText("Next >>")
        self.display_recipe_count_label.setText("Displaying")

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
