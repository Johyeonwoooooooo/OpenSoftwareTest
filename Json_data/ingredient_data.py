import re

file_path = "C:/OpenSoftware_test/recipe_ingredients.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read().strip()

ingredients_list = re.split(r'\s+', data)

ingredient_count_list = [(ingredients_list[i], ingredients_list[i+1]) for i in range(23000, len(ingredients_list) - 1, 2)]

print(ingredient_count_list)
