import numpy as np
import re
import pickle

file_path = "C:\\OpenSoftware_test\\recipe_ingredients.txt" # labtop

recipes = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line: 
            line = re.split(r'\s+', line)
            recipe = [line[i] for i in range(0, len(line), 2)]
            recipes.append(recipe)


with open('ingredient_based_recommend_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

similarities = loaded_model.score(['파스타면', '바질'])


most_similar_indices = np.argsort(similarities)[::-1][:5]
print("Most similar recipes (top 5):")
for index in most_similar_indices:
    print(recipes[index])