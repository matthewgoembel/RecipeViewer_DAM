from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QSizePolicy, QFrame, QFormLayout, QDialog
)


class RecipeDetails(QDialog):
    def __init__(self, recipe, parent=None):
        super().__init__(parent)

        self.recipe = recipe
        self.setup_ui()
        self.setWindowTitle("Recipe Details")
        self.setMinimumSize(400, 480)
        self.setAutoFillBackground(False)
        self.setStyleSheet(
            "background-color: rgb(238, 238, 238);\n"
            "background-color: rgb(236, 235, 237);"
        )

        self.show()

    def setup_ui(self):
        # Make recipe card layout
        self.recipe_card = QWidget(self)
        self.recipe_card_layout = QVBoxLayout(self.recipe_card)
        self.recipe_card_layout.setContentsMargins(0, 0, 0, 0)
        self.recipe_card_layout.setSpacing(7)
        self.recipe_card.setMinimumSize(300, 400)

        # Set the recipe images
        self.recipe_image = QLabel(self)
        self.recipe_image.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.recipe_image.setScaledContents(True)

        pixmap = self.recipe.get_image()
        if pixmap is not None:
            self.recipe_image.setPixmap(pixmap)
        else:
            blank_pixmap = QPixmap(self.recipe_card.width(), self.recipe_card.height() // 2)
            blank_pixmap.fill(QtCore.Qt.transparent)
            self.recipe_image.setPixmap(blank_pixmap)

        self.recipe_image.setFrameShape(QFrame.Panel)
        self.recipe_image.setFrameShadow(QFrame.Sunken)
        self.recipe_image.setAlignment(QtCore.Qt.AlignCenter)
        self.recipe_card_layout.addWidget(self.recipe_image)

        # Set the recipe info form layout and design
        self.recipe_info_form_layout = QFormLayout()
        self.recipe_info_form_layout.setLabelAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.recipe_info_form_layout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.recipe_info_form_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.recipe_info_form_layout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.recipe_info_form_layout.setContentsMargins(0, 1, 0, 1)
        self.recipe_info_form_layout.setVerticalSpacing(7)

        # Recipe number
        self.recipe_num_label = QLabel("Recipe #:               ")
        self.recipe_num_label.setFrameShape(QFrame.Panel)
        self.recipe_num_label.setFrameShadow(QFrame.Sunken)
        self.recipe_num_info = QLabel(str(self.recipe.get_recipe_number()))
        self.recipe_num_info.setFrameShape(QFrame.Panel)
        self.recipe_num_info.setFrameShadow(QFrame.Sunken)

        # Recipe name
        self.recipe_name_label = QLabel("Recipe Name:         ")
        self.recipe_name_label.setFrameShape(QFrame.Panel)
        self.recipe_name_label.setFrameShadow(QFrame.Sunken)
        self.recipe_name_info = QLabel(self.recipe.get_name())
        self.recipe_name_info.setFrameShape(QFrame.Panel)
        self.recipe_name_info.setFrameShadow(QFrame.Sunken)
        self.recipe_name_info.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum))
        self.recipe_name_info.setWordWrap(True)

        # Prep time
        self.prep_time_label = QLabel("Prep Time:             ")
        self.prep_time_label.setFrameShape(QFrame.Panel)
        self.prep_time_label.setFrameShadow(QFrame.Sunken)
        self.prep_time_info = QLabel(self.recipe.get_prep_time())
        self.prep_time_info.setFrameShape(QFrame.Panel)
        self.prep_time_info.setFrameShadow(QFrame.Sunken)

        # Cook time
        self.cook_time_label = QLabel("Cook Time:            ")
        self.cook_time_label.setFrameShape(QFrame.Panel)
        self.cook_time_label.setFrameShadow(QFrame.Sunken)
        self.cook_time_info = QLabel(self.recipe.get_cook_time())
        self.cook_time_info.setFrameShape(QFrame.Panel)
        self.cook_time_info.setFrameShadow(QFrame.Sunken)

        # Description
        self.description_label = QLabel("Description:          ")
        self.description_label.setFrameShape(QFrame.Panel)
        self.description_label.setFrameShadow(QFrame.Sunken)
        self.description_info = QLabel(self.recipe.get_description())
        self.description_info.setFrameShape(QFrame.Panel)
        self.description_info.setFrameShadow(QFrame.Sunken)
        self.description_info.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum))
        self.description_info.setWordWrap(True)

        # Ingredients
        self.ingredients_label = QLabel("Ingredients:          ")
        self.ingredients_label.setFrameShape(QFrame.Panel)
        self.ingredients_label.setFrameShadow(QFrame.Sunken)
        ingredients = '\n'.join(self.recipe.get_ingredients())
        self.ingredients_info = QLabel(ingredients)
        self.ingredients_info.setFrameShape(QFrame.Panel)
        self.ingredients_info.setFrameShadow(QFrame.Sunken)
        self.ingredients_info.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum))
        self.ingredients_info.setWordWrap(True)

        # Add the form layout rows
        self.recipe_info_form_layout.addRow(self.recipe_num_label, self.recipe_num_info)
        self.recipe_info_form_layout.addRow(self.recipe_name_label, self.recipe_name_info)
        self.recipe_info_form_layout.addRow(self.prep_time_label, self.prep_time_info)
        self.recipe_info_form_layout.addRow(self.cook_time_label, self.cook_time_info)
        self.recipe_info_form_layout.addRow(self.description_label, self.description_info)
        self.recipe_info_form_layout.addRow(self.ingredients_label, self.ingredients_info)

        self.recipe_card_layout.addLayout(self.recipe_info_form_layout)
        self.setLayout(self.recipe_card_layout)
