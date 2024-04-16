import json

from recipe import Recipe


class RecipeProcessor:
    def __init__(self):
        self.recipes = []

    def load_recipes(self, json_file):
        with open(json_file, 'r', encoding="utf-8") as file:
            recipes_data = json.load(file)
            for recipe_data in recipes_data:
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

    def get_recipes(self):
        return self.recipes
