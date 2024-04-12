import json

from Recipe import Recipe


class RecipeProcessor:
    def __init__(self):
        self.recipes = []

    def load_recipes(self, json_file):
        with open(json_file, 'r') as file:
            recipes_data = json.load(file)
            for recipe_data in recipes_data:
                recipe = Recipe(
                    recipe_data['name'],
                    recipe_data['cookTime'],
                    recipe_data['prepTime'],
                    recipe_data['recipeYield'],
                    recipe_data['imageURL']
                )
                self.recipes.append(recipe)

    def get_recipes(self):
        return self.recipes
