from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout,
    QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QGridLayout, QSizePolicy, QFrame, QFormLayout, QLayout
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
        self.layout_ui()  # Set up the UI layout
        self.recipe_widget_list = self.populate_recipe_cards()
        self.setup_window()  # Set up the main window
        self.setup_connections()  # Set up event listeners
        self.update_recipe_layout(self.recipe_widget_list[:self.recipes_per_page], 0, self.recipes_per_page)

        self.show()

    def setup_window(self):
        """
        Set up properties for the main window.
        """
        self.setWindowTitle("Recipe Viewer")
        self.setMinimumSize(900, 840)
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
        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setVerticalSpacing(7)

        # Create the main grid layout for the UI elements
        self.main_grid_layout = QGridLayout()
        self.main_grid_layout.setHorizontalSpacing(10)
        self.main_grid_layout.setVerticalSpacing(0)

        # Set minimum sizes for the grid layout cells
        self.main_grid_layout.setColumnMinimumWidth(0, 620)
        self.main_grid_layout.setRowMinimumHeight(1, 700)

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
        self.main_grid_layout.addWidget(
            self.display_recipe_count_label, 3, 0, 1, 1, alignment=QtCore.Qt.AlignBottom
        )

        # Navigation buttons layout
        self.page_button_layout = QHBoxLayout()
        self.page_button_layout.setContentsMargins(0, 5, 20, 15)
        self.page_button_layout.setSpacing(10)

        # Spacer item for alignment
        v_spacer = QWidget()
        v_spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.page_button_layout.addWidget(v_spacer)

        # Create navigation buttons
        self.prev_button = QPushButton("<< Previous", self.central_widget)
        self.prev_button.setFixedSize(QtCore.QSize(100, 20))
        self.prev_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_button_layout.addWidget(self.prev_button)

        self.first_button = QPushButton("First", self.central_widget)
        self.first_button.setFixedSize(QtCore.QSize(70, 20))
        self.first_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_button_layout.addWidget(self.first_button)

        self.last_button = QPushButton("Last", self.central_widget)
        self.last_button.setFixedSize(QtCore.QSize(60, 20))
        self.last_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_button_layout.addWidget(self.last_button)

        self.next_button = QPushButton("Next >>", self.central_widget)
        self.next_button.setFixedSize(QtCore.QSize(100, 20))
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
        self.search_button.setFixedSize(QtCore.QSize(80, 20))
        self.search_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_bar_layout.addWidget(self.search_button)

        # Create reset button
        self.reset_button = QPushButton("Reset", self.central_widget)
        self.reset_button.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
        self.reset_button.setFixedSize(QtCore.QSize(80, 20))
        self.reset_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_bar_layout.addWidget(self.reset_button)

        # Add search bar elements to the main grid layout
        self.main_grid_layout.addLayout(self.search_bar_layout, 0, 0, 1, 1)

        # Recipe grid layout
        self.recipe_grid_layout = QGridLayout()
        self.recipe_grid_layout.setRowMinimumHeight(0, 400)
        self.recipe_grid_layout.setRowMinimumHeight(1, 400)
        self.recipe_grid_layout.setColumnMinimumWidth(0, 300)
        self.recipe_grid_layout.setColumnMinimumWidth(1, 300)
        self.recipe_grid_layout.setColumnMinimumWidth(2, 300)
        self.recipe_grid_layout.setColumnMinimumWidth(3, 300)
        self.recipe_grid_layout.setContentsMargins(15, 5, 15, 30)
        self.recipe_grid_layout.setHorizontalSpacing(20)
        self.recipe_grid_layout.setVerticalSpacing(50)
        self.main_grid_layout.addLayout(self.recipe_grid_layout, 1, 0, 1, 1)

        # Add main grid layout to the central widget's grid layout
        self.grid_layout.addLayout(self.main_grid_layout, 0, 0, 1, 1)
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

    def populate_recipe_cards(self):
        recipe_widget_list = []

        self.display_recipe_count_label.setText(
            f"Displaying 1-{self.recipes_per_page} of {self.total_recipe_count} recipes")
        for recipe in self.recipe_list:
            # Make recipe card layouts
            recipe_card = QWidget()
            recipe_card_layout = QVBoxLayout(recipe_card)
            recipe_card_layout.setContentsMargins(0, 0, 0, 0)
            recipe_card_layout.setSpacing(7)
            recipe_card.setMinimumSize(200, 300)

            # Set the recipe images
            recipe_image = QLabel(self)
            recipe_image.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            recipe_image.setScaledContents(True)

            pixmap = recipe.get_image()
            if pixmap is not None:
                recipe_image.setPixmap(pixmap)
            else:
                blank_pixmap = QPixmap(recipe_card.width(), recipe_card.height()//2)
                blank_pixmap.fill(QtCore.Qt.transparent)
                recipe_image.setPixmap(blank_pixmap)

            recipe_image.setFrameShape(QFrame.Panel)
            recipe_image.setFrameShadow(QFrame.Sunken)
            recipe_image.setAlignment(QtCore.Qt.AlignCenter)
            recipe_card_layout.addWidget(recipe_image)

            # Set the recipe info form layout and design
            recipe_info_form_layout = QFormLayout()
            recipe_info_form_layout.setLabelAlignment(
                QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            recipe_info_form_layout.setFormAlignment(QtCore.Qt.AlignCenter)
            recipe_info_form_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
            recipe_info_form_layout.setRowWrapPolicy(QFormLayout.DontWrapRows)
            recipe_info_form_layout.setContentsMargins(0, 5, 0, 5)
            recipe_info_form_layout.setVerticalSpacing(7)

            # Recipe number
            recipe_num_label = QLabel("Recipe #:               ")
            recipe_num_label.setFrameShape(QFrame.Panel)
            recipe_num_label.setFrameShadow(QFrame.Sunken)
            recipe_num_info = QLabel(str(recipe.get_recipe_number()))
            recipe_num_info.setFrameShape(QFrame.Panel)
            recipe_num_info.setFrameShadow(QFrame.Sunken)

            # Recipe name
            recipe_name_label = QLabel("Recipe Name:         ")
            recipe_name_label.setFrameShape(QFrame.Panel)
            recipe_name_label.setFrameShadow(QFrame.Sunken)
            recipe_name_info = QLabel(recipe.get_name())
            recipe_name_info.setFrameShape(QFrame.Panel)
            recipe_name_info.setFrameShadow(QFrame.Sunken)
            recipe_name_info.setSizePolicy(QSizePolicy)
            recipe_name_info.setWordWrap(True)

            # Prep time
            prep_time_label = QLabel("Prep Time:             ")
            prep_time_label.setFrameShape(QFrame.Panel)
            prep_time_label.setFrameShadow(QFrame.Sunken)
            prep_time_info = QLabel(recipe.get_prep_time())
            prep_time_info.setFrameShape(QFrame.Panel)
            prep_time_info.setFrameShadow(QFrame.Sunken)

            # Cook time
            cook_time_label = QLabel("Cook Time:            ")
            cook_time_label.setFrameShape(QFrame.Panel)
            cook_time_label.setFrameShadow(QFrame.Sunken)
            cook_time_info = QLabel(recipe.get_cook_time())
            cook_time_info.setFrameShape(QFrame.Panel)
            cook_time_info.setFrameShadow(QFrame.Sunken)

            # Add the form layout rows
            recipe_info_form_layout.addRow(recipe_num_label, recipe_num_info)
            recipe_info_form_layout.addRow(recipe_name_label, recipe_name_info)
            recipe_info_form_layout.addRow(prep_time_label, prep_time_info)
            recipe_info_form_layout.addRow(cook_time_label, cook_time_info)

            # Add the 'View Recipe' button with a spacer to the left
            h_spacer = QWidget()
            h_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            view_recipe_button = QPushButton("View Recipe")
            view_recipe_button.setStyleSheet("background-color: rgb(255, 255, 255);")
            view_recipe_button.setFixedSize(100, 20)
            view_recipe_button.setContentsMargins(0, 15, 20, 15)
            recipe_info_form_layout.addRow(h_spacer, view_recipe_button)

            # Add the new components to the layout and add that to the widget list
            recipe_card_layout.addLayout(recipe_info_form_layout)
            recipe_widget_list.append(recipe_card)

        print("Recipe widget list:", recipe_widget_list)  # Debug print
        return recipe_widget_list

    def update_recipe_layout(self, recipes, start_index, end_index):
        """
        Update the layout with a new set of recipes.
        """
        print("Recipes: ", recipes)
        self.display_recipe_count_label.clear()
        self.display_recipe_count_label.setText(
            f"Displaying {start_index + 1}-{end_index} of {self.total_recipe_count} recipes")

        print("Before removing widgets. Count:", self.recipe_grid_layout.count())  # Debug print

        # Clear the layout
        while self.recipe_grid_layout.count():
            item = self.recipe_grid_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.hide()  # Hide the widget instead of deleting it

        print("After removing widgets. Count:", self.recipe_grid_layout.count())  # Debug print
        max_widgets = min(len(recipes), self.recipes_per_page)
        print("Max widget = ", max_widgets)

        row = 0
        col = 0
        for i in range(max_widgets):
            recipe_widget = recipes[i]
            print("Adding widget at row:", row, "col:", col)  # Debug print
            print("Recipe widget: ", recipe_widget)
            self.recipe_grid_layout.addWidget(recipe_widget, row, col)
            recipe_widget.show()  # Make sure the widget is visible
            print("Got added")
            col += 1
            if col == 4:
                col = 0
                row += 1

        # Ensure that the layout is added back to the central widget
        self.central_widget.setLayout(self.recipe_grid_layout)

    def next(self):
        # Display next set of recipes
        first_index = (self.current_page * self.recipes_per_page)
        last_index = min(first_index + self.recipes_per_page + 1, self.total_recipe_count)
        if last_index < self.total_recipe_count:
            self.current_page += 1
            self.update_recipe_layout(self.recipe_widget_list[first_index:last_index],
                                      first_index, last_index)
        else:
            self.last()

    def previous(self):
        # Display previous set of recipes
        last_index = (self.current_page - 1) * self.recipes_per_page
        if last_index > 0:
            first_index = max(last_index - self.recipes_per_page, 0)
            self.current_page -= 1
            self.update_recipe_layout(self.recipe_widget_list[first_index:last_index],
                                      first_index, last_index)
        else:
            self.first()

    def first(self):
        # Jump to beginning of recipe list
        self.current_page = 1
        self.update_recipe_layout(self.recipe_widget_list[:self.recipes_per_page + 1],
                                  0, self.recipes_per_page)

    def last(self):
        # Jump to end of recipe list
        self.current_page = self.total_recipe_count // self.recipes_per_page
        self.update_recipe_layout(self.recipe_widget_list[0 - self.recipes_per_page:],
                                  self.total_recipe_count - self.recipes_per_page,
                                  self.total_recipe_count)

    def search(self):
        # Search for recipes containing keywords
        search_text = self.search_line.text()

    def reset(self):
        # Clear search results and return to normal pagination
        self.search_line.setText('')
        self.first()
