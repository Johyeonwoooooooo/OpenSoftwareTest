import pickle
import re
from gensim.models import Word2Vec
import numpy as np

# file_path = "C:\\OSSP\\OpenSoftwareTest\\recipe_ingredients.txt" # desktop
file_path = "C:\\OpenSoftware_test\\recipe_ingredients.txt" # labtop

recipes_ingredient = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line: 
            line = re.split(r'\s+', line)
            recipe = [line[i] for i in range(0, len(line), 2)]
            recipes_ingredient.append(recipe)

class IBRM:
    def __init__(self):
        self.word2vec = Word2Vec(sentences=recipes_ingredient, vector_size=100, window=28, min_count=1, workers=4)
        self.recommendation_list = [0 for i in range(len(recipes_ingredient))]
        self.embedded_recipes = [self.embed_recipe(recipe) for recipe in recipes_ingredient]
    
    def cosine_similarity(self, vec1, vec2):
        dot_product = np.dot(vec1, vec2)
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)
        return dot_product / (norm_vec1 * norm_vec2)
    
    def embed_recipe(self, recipe):
        embedding = []
        for word in recipe:
            if word in self.word2vec.wv.key_to_index:
                embedding.append(self.word2vec.wv[word])
        if len(embedding) == 0:
            return np.zeros(self.word2vec.vector_size)
        return np.mean(np.array(embedding), axis=0)

    def score(self, ingredients):
        if ingredients == []:
            return [0 for i in range(100)]
        ingredient_vector = self.embed_recipe(recipe=ingredients)
        similarities = [self.cosine_similarity(ingredient_vector, embedded_recipe) for embedded_recipe in self.embedded_recipes]
        return similarities
    

ingredient_recommend_model = IBRM()
with open('ingredient_based_recommend_model.pkl', 'wb') as file:
    pickle.dump(ingredient_recommend_model, file)
