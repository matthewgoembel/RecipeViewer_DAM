from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

def format_time(time_str):
    hours, minutes = time_str.strip("PT").strip("M").split("H")
    hours = int(hours)
    minutes = int(minutes)
    return f"{hours:02d}:{minutes:02d}"

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
        return format_time(self.cook_time)

    def get_prep_time(self):
        # Implement prep time formatting
        return format_time(self.prep_time)

    def get_ingredients(self):
        return self._ingredients

    def get_image(self):
        # Return image 
        return self._image

    def set_image(self, url):
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # For downloading progress

        # Testing
        if total_size == 0:
            raise ValueError("Invalid URL or empty content")

        # Create QPixmap to display the image
        pixmap = QPixmap()

        # Download the image with progress
        downloaded_size = 0
        for data in response.iter_content(block_size):
            downloaded_size += len(data)
            pixmap.loadFromData(data)
            # Update the loading progress in the command line
            self.progress_bar(downloaded_size, total_size, prefix='Downloading:', suffix='Complete', length=50)

        # Show the image after downloading completes
        label = QLabel()
        label.setPixmap(pixmap)
        label.show()

    def progress_bar(self, iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='', flush=True)
        if iteration == total:
            print()
