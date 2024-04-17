from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
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
        try:
            print("Downloading Recipe Image")
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content length header
                return None

            else:
                # Create QPixmap to display the image
                pixmap = QPixmap()
                # Download the image with progress
                dl = 0
                total_length = int(total_length)
                progress_bar_length = total_length // 1024  # Adjust this to suit your progress bar size
                with tqdm(total=progress_bar_length, unit='KB', file=sys.stdout) as pbar:
                    with open(url.split('/')[-1], "wb") as f:
                        for data in response.iter_content(chunk_size=4096):
                            dl += len(data)
                            f.write(data)
                            pbar.update(len(data) // 1024)  # Update progress bar
                # Load image data into QPixmap
                pixmap.loadFromData(open(url.split('/')[-1], "rb").read())
                return pixmap

        except requests.HTTPError as e:
            print(f"HTTP Error occurred: {e}")
        except requests.ConnectionError as e:
            print(f"Connection Error occurred: {e}")
        except ValueError as e:
            print(f"ValueError occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
