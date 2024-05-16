import re
import pickle

file_path = "C:\\OpenSoftware_test\\Json_data\\recipe_ingredients.txt" #labtop

with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read().strip()

ingredients_list = re.split(r'\s+', data)

ingredient_index = dict()
index = 0
for i in range(0, len(ingredients_list), 2):
    if(ingredients_list[i] not in ingredient_index):
        ingredient_index[ingredients_list[i]] = index
        index += 1

print(ingredient_index.keys())
#print(len(ingredient_index)) 

with open('ingredientList.txt', 'w', encoding='utf-8') as file:
     for name in ingredient_index.keys():
         file.write(name + '\n')