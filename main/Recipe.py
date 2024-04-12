class Recipe:
    def __init__(self, name, cook_time, prep_time, recipe_yield, image_url):
        self.name = name
        self.cook_time = cook_time
        self.prep_time = prep_time
        self.recipe_yield = recipe_yield
        self.image_url = image_url

    def get_name(self):
        return self.name

    def get_cook_time(self):
        # Implement cook time formatting
        pass

    def get_prep_time(self):
        # Implement prep time formatting
        pass

    def get_recipe_yield(self):
        return self.recipe_yield

    def set_image(self, url):
        # Implement image download and display
        pass

    def get_image(self):
        # Return image file name
        pass
