from PyQt5.QtGui import QPixmap
import requests


def format_time(time_str):
    if time_str != '':
        # Split the string at 'H' if present, then split the second part at 'M'
        parts = time_str.split('H')[-1].split('M')

        # Extract hours and minutes from the split parts
        hours = 0
        minutes = 0
        if len(parts) > 1:
            if len(parts) == 2:
                minutes = int(''.join(filter(str.isdigit, parts[0])))
            else:
                hours = int(''.join(filter(str.isdigit, parts[0])))
                minutes = int(''.join(filter(str.isdigit, parts[1])))

        # Format the hours and minutes as strings with leading zeros
        return f"{hours:02d}:{minutes:02d}"
    else:
        return "00:00"


class Recipe:
    recipe_number_counter = 1

    def __init__(self, name, description, image_url, recipe_yield, cook_time, prep_time, ingredients):
        self._recipe_number = self.recipe_number_counter
        Recipe.recipe_number_counter += 1
        self._name = name
        self._description = description
        self._recipe_yield = recipe_yield
        self._cook_time = cook_time
        self._prep_time = prep_time
        self._ingredients = ingredients
        self._image = self.set_image(image_url)

    def get_recipe_number(self):
        return self._recipe_number

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_recipe_yield(self):
        return self._recipe_yield

    def get_cook_time(self):
        # Implement cook time formatting
        return format_time(self._cook_time)

    def get_prep_time(self):
        # Implement prep time formatting
        return format_time(self._prep_time)

    def get_ingredients(self):
        return self._ingredients

    def get_image(self):
        # Return image 
        return self._image

    def set_image(self, url):
        response = requests.get(url, stream=True)

        # Create QPixmap to display the image
        pixmap = QPixmap()

        # Download the image
        image_data = b''  # Initialize image data
        for data in response:
            image_data += data

        # Load image data into QPixmap
        pixmap.loadFromData(image_data)
        return pixmap
