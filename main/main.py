from RecipeUI import RecipeUI
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    recipe_ui = RecipeUI()
    recipe_ui.show()
    app.exec()


main()
