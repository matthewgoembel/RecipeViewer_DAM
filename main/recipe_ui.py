import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout,
    QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QGridLayout, QSizePolicy
)
from recipe_processor import RecipeProcessor


class RecipeUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_page = 1
        self.recipes_per_page = 8
        recipe_processor = RecipeProcessor()
        recipe_processor.load_recipes(r"../recipe_data/recipes.json")
        self.recipe_list = recipe_processor.get_recipes()
        self.total_recipe_count = len(self.recipe_list)
        self.recipe_widgets = []  # List to store recipe widgets
        self.setup_window()  # Set up the main window
        self.layout_ui()  # Set up the UI layout
        self.setup_connections()  # Set up event listeners

    def setup_window(self):
        """
        Set up properties for the main window.
        """
        self.setWindowTitle("Recipe Viewer")
        self.setGeometry(QtCore.QRect(300, 100, 1090, 848))
        self.setAutoFillBackground(False)
        # Set background color
        self.setStyleSheet(
            "background-color: rgb(238, 238, 238);\n"
            "background-color: rgb(236, 235, 237);"
        )

    def layout_ui(self):
        """
        Create and arrange the UI elements.
        """
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a grid layout for the central widget
        self.gridLayout = QGridLayout(self.central_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(7)

        # Create the main grid layout for the UI elements
        self.main_grid_layout = QGridLayout()
        self.main_grid_layout.setSizeConstraint(QVBoxLayout.SetNoConstraint)
        self.main_grid_layout.setHorizontalSpacing(10)
        self.main_grid_layout.setVerticalSpacing(0)

        # Display recipe count label
        self.display_recipe_count_label = QLabel(self.central_widget)
        self.display_recipe_count_label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0.966, "
            "x2:0.995, y2:0.119773, stop:0 rgba(134, 134, 134, 255), "
            "stop:1 rgba(234, 234, 234, 255));"
        )
        self.display_recipe_count_label.setFrameShape(QLabel.Box)
        self.display_recipe_count_label.setFrameShadow(QLabel.Plain)
        self.display_recipe_count_label.setFixedHeight(30)
        self.display_recipe_count_label.setText("Displaying")
        self.main_grid_layout.addWidget(
            self.display_recipe_count_label, 3, 0, 1, 1, alignment=QtCore.Qt.AlignBottom
        )

        # Navigation buttons layout
        self.page_button_layout = QHBoxLayout()
        self.page_button_layout.setContentsMargins(0, 5, 20, 15)
        self.page_button_layout.setSpacing(10)

        # Spacer item for alignment
        spacerItem = QWidget()
        spacerItem.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.page_button_layout.addWidget(spacerItem)

        # Create navigation buttons
        self.prev_button = QPushButton("<< Previous", self.central_widget)
        self.prev_button.setMaximumSize(QtCore.QSize(100, 20))
        self.prev_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_button_layout.addWidget(self.prev_button)

        self.first_button = QPushButton("First", self.central_widget)
        self.first_button.setMaximumSize(QtCore.QSize(70, 20))
        self.first_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_button_layout.addWidget(self.first_button)

        self.last_button = QPushButton("Last", self.central_widget)
        self.last_button.setMaximumSize(QtCore.QSize(60, 20))
        self.last_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_button_layout.addWidget(self.last_button)

        self.next_button = QPushButton("Next >>", self.central_widget)
        self.next_button.setMaximumSize(QtCore.QSize(100, 20))
        self.next_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_button_layout.addWidget(self.next_button)

        # Add navigation buttons to the main grid layout
        self.main_grid_layout.addLayout(self.page_button_layout, 2, 0, 1, 1)

        # Search bar layout
        self.search_bar_layout = QHBoxLayout()
        self.search_bar_layout.setContentsMargins(10, 10, 10, 15)
        self.search_bar_layout.setSpacing(10)

        # Create search line edit widget
        self.search_line = QLineEdit(self.central_widget)
        self.search_line.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
        self.search_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_bar_layout.addWidget(self.search_line)

        # Create search button
        self.search_button = QPushButton("Search", self.central_widget)
        self.search_button.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
        self.search_button.setMaximumSize(QtCore.QSize(80, 20))
        self.search_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_bar_layout.addWidget(self.search_button)

        # Create reset button
        self.reset_button = QPushButton("Reset", self.central_widget)
        self.reset_button.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
        self.reset_button.setMaximumSize(QtCore.QSize(80, 20))
        self.reset_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_bar_layout.addWidget(self.reset_button)

        # Add search bar elements to the main grid layout
        self.main_grid_layout.addLayout(self.search_bar_layout, 0, 0, 1, 1)

        # Recipe grid layout
        self.recipe_grid_layout = QGridLayout()
        self.recipe_grid_layout.setRowMinimumHeight(0, 300)
        self.recipe_grid_layout.setRowMinimumHeight(1, 300)
        self.recipe_grid_layout.setColumnMinimumWidth(0, 200)
        self.recipe_grid_layout.setColumnMinimumWidth(1, 200)
        self.recipe_grid_layout.setColumnMinimumWidth(2, 200)
        self.recipe_grid_layout.setColumnMinimumWidth(3, 200)
        self.recipe_grid_layout.setContentsMargins(10, 5, 10, 30)
        self.recipe_grid_layout.setHorizontalSpacing(15)
        self.recipe_grid_layout.setVerticalSpacing(40)
        self.main_grid_layout.addLayout(self.recipe_grid_layout, 1, 0, 1, 1)

        # Add main grid layout to the central widget's grid layout
        self.gridLayout.addLayout(self.main_grid_layout, 0, 0, 1, 1)
        self.setCentralWidget(self.central_widget)

    def setup_connections(self):
        """
        Set up connections for button clicks and search bar return pressed.
        """
        # Connect buttons' clicked signals to their respective methods
        self.first_button.clicked.connect(self.first)
        self.last_button.clicked.connect(self.last)
        self.next_button.clicked.connect(self.next)
        self.prev_button.clicked.connect(self.previous)
        self.reset_button.clicked.connect(self.reset)

        # Connect search line edit's returnPressed signal to search method
        self.search_line.returnPressed.connect(self.search)

    def update_recipe_layout(self):
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

    def search(self):
        # Search for recipes containing keywords
        search_text = self.search_line.text()

    def reset(self):
        # Clear search results and return to normal pagination
        self.search_line.setText('')
