import re
import pickle

# with open('ingredient_index.pkl', 'rb') as file:
#     ingredient_dict = pickle.load(file)

# class Vectorizer:
#     def __init__(self):
#         self.map = ingredient_dict
    
#     def vectorize(self, ingredients):
#         vector = [0 for i in range(len(self.map.keys()))]
        
#         ingredient_list = ingredients.split()
#         for ingredient in ingredient_list:
#             idx = self.map[ingredient]
#             vector[idx] = 1

#         return vector
    
file_path = "C:\\OSSP\\OpenSoftwareTest\\recipe_ingredients.txt" # desktop
# file_path = "C:/OpenSoftware_test/recipe_ingredients.txt"   # laptop

data = []
with open(file_path, 'r', encoding='utf-8') as file:
    while True:
        line = file.readline().strip()

        if not line: 
            break

        line = re.split(r'\s+', line)
        ingredient =  ' '.join([line[i] for i in range(0, len(line), 2)])
        data.append(ingredient)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(data)

print(tfidf_matrix)

cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix)

# 가장 유사한 다른 레시피 인덱스 찾기
most_similar_index = cosine_sim.argsort()[0][-2]  # 가장 유사한 레시피는 제외
print("가장 유사한 레시피 인덱스:", most_similar_index)
print("0번 레시피 사용 재료 : ", data[0])
print("가장 유사한 레시피:", data[most_similar_index])


my_ingredient = ['설탕 소금 돼지고기 김치']
my_vector = tfidf_vectorizer.transform(my_ingredient)
my_sim = cosine_similarity(my_vector, tfidf_matrix)
my_sim_index = my_sim.argsort()[0][-2]
print(data[my_sim_index])