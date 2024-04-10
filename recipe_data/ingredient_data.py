import re
import pickle

# file_path = "C:/OpenSoftware_test/recipe_ingredients.txt" #labtop
file_path = "C:\\OSSP\\OpenSoftwareTest\\recipe_ingredients.txt" #desktop
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read().strip()

ingredients_list = re.split(r'\s+', data)

ingredient_index = dict()
index = 0
for i in range(0, len(ingredients_list), 2):
    if(ingredients_list[i] not in ingredient_index):
        ingredient_index[ingredients_list[i]] = index
        index += 1

# ingredient_count_list = [(ingredients_list[i], ingredients_list[i+1]) for i in range(23000, len(ingredients_list), 2)]

# print(ingredient_count_list)

print(ingredient_index.keys())
# print(len(ingredient_index))

with open('ingredient_index.pkl', 'wb') as file:
    pickle.dump(ingredient_index, file)