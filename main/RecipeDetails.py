from PyQt5.QtWidgets import QDialog


class RecipeDetails(QDialog):
    def __init__(self, recipe):
        super().__init__()
        self.setWindowTitle("Recipe Details")
        self.setup_ui(recipe)

    def setup_ui(self, recipe):
        pass
