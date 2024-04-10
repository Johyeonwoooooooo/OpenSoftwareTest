import pickle

with open('recipe_word2vec_model.pkl', 'rb') as file:
    model = pickle.load(file)
