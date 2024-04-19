import json
import time

import requests
from recipe import Recipe


class RecipeProcessor:
    def __init__(self):
        self.recipes = []
        self.slashes = ['/', '_', '\\']
        self.PURPLE = "\033[35m"
        self.GREEN = "\033[32m"
        self.RESET = "\033[0m"
        self.BOLD = "\033[1m"

        self.GROUP_NAME = \
            ("Darian, Anthony, Matthew\n"
             f"{' ' * 27}D.A.M")
        self.ASCII_LOAD = \
            (" ____    _    __  __ \n"
             "|  _ \  / \  |  \/  |\n"
             "| | | |/ _ \ | |\/| |\n"
             "| |_| / ___ \| |  | |\n"
             "|____/_/   \_\_|  |_|  ")
        self.APP_NAME = \
            (" ____                          __     __                         \n"
             "|  _ \ ___  ___(_) ____   ___  \ \   / (_) _____      _____ _____\n"
             "| |_) / _ \/ __| || ._ \ / _ \  \ \ / /| |/ _ \ \ /\ / / _ \| ,__|\n"
             "|  _ <  __/ (__| || |_) |  __/   \ V / | |  __/\ V  V /  __/| |   \n"
             "|_| \_\___|\___|_|| ,__/ \___|    \_/  |_|\___| \_/\_/ \___||_|   \n"
             "               |_||_|                                                ")

    def load_recipes(self, json_file):

        print(self.PURPLE, self.BOLD, ' ' * 15, self.GROUP_NAME)
        print(self.APP_NAME, self.RESET, "\n")

        with open(json_file, 'r', encoding="utf-8") as file:
            recipes_data = json.load(file)
            for index, recipe_data in enumerate(recipes_data):
                try:
                    response = requests.get(recipe_data['image'])

                    print('\r', self.GREEN,
                          f"{self.slashes[index % 3]} Validating Recipe image {index} of {len(recipes_data)}", end="")

                    if response.status_code == 200:
                        recipe = Recipe(
                            recipe_data['name'],
                            recipe_data['description'],
                            recipe_data['image'],
                            recipe_data['recipeYield'],
                            recipe_data['cookTime'],
                            recipe_data['prepTime'],
                            recipe_data['ingredients']
                        )
                        self.recipes.append(recipe)
                except requests.ConnectionError:
                    pass
                except requests.HTTPError:
                    pass

    def get_recipes(self):
        return self.recipes
