import pickle
import re
from modelByIngredient import IBRM 
from gensim.models import Word2Vec

file_path = "C:\\OpenSoftware_test\\recipe_ingredients.txt"
recipes_ingredient = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            line = re.split(r'\s+', line)
            recipe = [line[i] for i in range(0, len(line), 2)]
            recipes_ingredient.append(recipe)


ingredient_recommend_model = IBRM(recipes_ingredient)

with open('ingredient_based_recommend_model.pkl', 'wb') as file:
    pickle.dump(ingredient_recommend_model, file)
