import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, \
        QVBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout, QSizePolicy


class RecipeUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()  # Set up the main window
        self.layout_ui()     # Set up the UI layout

    def setup_window(self):
        """
        Set up properties for the main window.
        """
        self.setWindowTitle("Recipe Viewer")
        self.setGeometry(QtCore.QRect(300, 100, 1090, 848))
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                           "background-color: rgb(236, 235, 237);")

    def layout_ui(self):
        """
        Create and arrange the UI elements.
        """
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.gridLayout = QGridLayout(self.central_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(7)

        self.main_grid_layout = QGridLayout()
        self.main_grid_layout.setSizeConstraint(QVBoxLayout.SetNoConstraint)
        self.main_grid_layout.setHorizontalSpacing(10)
        self.main_grid_layout.setVerticalSpacing(0)

        # Display recipe count label
        self.display_recipe_count_label = QLabel(self.central_widget)
        self.display_recipe_count_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.966, "
                                                      "x2:0.995, y2:0.119773, stop:0 rgba(134, 134, 134, 255), "
                                                      "stop:1 rgba(234, 234, 234, 255));")
        self.display_recipe_count_label.setFrameShape(QLabel.Box)
        self.display_recipe_count_label.setFrameShadow(QLabel.Plain)
        self.display_recipe_count_label.setFixedHeight(30)
        self.display_recipe_count_label.setText("Displaying")
        self.main_grid_layout.addWidget(self.display_recipe_count_label, 3, 0, 1, 1, alignment=QtCore.Qt.AlignBottom)

        # Navigation buttons layout
        self.page_button_layout = QHBoxLayout()
        self.page_button_layout.setContentsMargins(0, 5, 20, 15)
        self.page_button_layout.setSpacing(10)

        # Spacer item for alignment
        spacerItem = QWidget()
        spacerItem.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.page_button_layout.addWidget(spacerItem)

        # Previous button
        self.prev_button = QPushButton("<< Previous", self.central_widget)
        self.prev_button.setMaximumSize(QtCore.QSize(100, 20))
        self.prev_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_button_layout.addWidget(self.prev_button)

        # First button
        self.first_button = QPushButton("First", self.central_widget)
        self.first_button.setMaximumSize(QtCore.QSize(70, 20))
        self.first_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_button_layout.addWidget(self.first_button)

        # Last button
        self.last_button = QPushButton("Last", self.central_widget)
        self.last_button.setMaximumSize(QtCore.QSize(60, 20))
        self.last_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_button_layout.addWidget(self.last_button)

        # Next button
        self.next_button = QPushButton("Next >>", self.central_widget)
        self.next_button.setMaximumSize(QtCore.QSize(100, 20))
        self.next_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_button_layout.addWidget(self.next_button)

        self.main_grid_layout.addLayout(self.page_button_layout, 2, 0, 1, 1)

        # Search bar layout
        self.search_bar_layout = QHBoxLayout()
        self.search_bar_layout.setContentsMargins(10, 10, 10, 15)
        self.search_bar_layout.setSpacing(10)

        self.search_line = QLineEdit(self.central_widget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.search_line.setSizePolicy(sizePolicy)
        self.search_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_bar_layout.addWidget(self.search_line)

        # Search button
        self.search_button = QPushButton("Search", self.central_widget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.search_button.setSizePolicy(sizePolicy)
        self.search_button.setMaximumSize(QtCore.QSize(80, 20))
        self.search_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_bar_layout.addWidget(self.search_button)

        # Reset button
        self.reset_button = QPushButton("Reset", self.central_widget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.reset_button.setSizePolicy(sizePolicy)
        self.reset_button.setMaximumSize(QtCore.QSize(80, 20))
        self.reset_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_bar_layout.addWidget(self.reset_button)

        self.main_grid_layout.addLayout(self.search_bar_layout, 0, 0, 1, 1)

        # Recipe grid layout
        self.recipe_grid_layout = QGridLayout()
        self.recipe_grid_layout.setSizeConstraint(QVBoxLayout.SetDefaultConstraint)
        self.recipe_grid_layout.setContentsMargins(10, 5, 10, 30)
        self.recipe_grid_layout.setHorizontalSpacing(15)
        self.recipe_grid_layout.setVerticalSpacing(40)
        self.main_grid_layout.addLayout(self.recipe_grid_layout, 1, 0, 1, 1)

        self.gridLayout.addLayout(self.main_grid_layout, 0, 0, 1, 1)
        self.setCentralWidget(self.central_widget)

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
