import pickle

with open('ingredient_index.pkl', 'rb') as file:
    loaded_ingredient_index = pickle.load(file)

print(loaded_ingredient_index)