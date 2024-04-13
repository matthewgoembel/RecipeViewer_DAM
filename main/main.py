from recipe_ui import RecipeUI
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    ui = RecipeUI()
    ui.show()
    sys.exit(app.exec_())


main()
