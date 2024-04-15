from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Recipe:
    def __init__(self, name, description, image_url, recipe_yield, cook_time, prep_time, ingredients):
        self._image = None

        self._name = name
        self._description = description
        self._recipe_yield = recipe_yield
        self._cook_time = cook_time
        self._prep_time = prep_time
        self._ingredients = ingredients

        self.set_image(image_url)

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_recipe_yield(self):
        return self._recipe_yield

    def get_cook_time(self):
        # Implement cook time formatting
        return self._cook_time

    def get_prep_time(self):
        # Implement prep time formatting
        return self._prep_time

    def get_ingredients(self):
        return self._ingredients

    def set_image(self, url):
        # Set image
        self._image = QPixmap(url).scaled(Qt.KeepAspectRatio)

    def get_image(self):
        # Return image 
        return self._image
