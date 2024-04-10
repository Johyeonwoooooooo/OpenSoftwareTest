import re
from gensim.models import Word2Vec
import numpy as np

file_path = "C:\\OSSP\\OpenSoftwareTest\\recipe_ingredients.txt"  # 파일 경로를 바꿔주세요

# 레시피 데이터 읽어오기
recipes = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:  # 빈 줄은 건너뜁니다
            line = re.split(r'\s+', line)
            recipe = [line[i] for i in range(0, len(line), 2)]
            recipes.append(recipe)

# Word2Vec 모델 학습
word2vec_model = Word2Vec(sentences=recipes, vector_size=100, window=5, min_count=1, workers=4)

def embed_recipe(recipe, model):
    embedding = []
    for word in recipe:
        if word in model:
            embedding.append(model[word])
    if len(embedding) == 0:
        return np.zeros(model.vector_size)  # Return zero vector if no word in the model
    return np.mean(embedding, axis=0)  # Take the mean of word embeddings

def embed_recipe_with_weights(recipe, model, weight_for_pasta):
    embedding = []
    for word in recipe:
        if word in model:
            # 파스타면과 같은 특정 재료일 경우 가중치 적용
            weight = weight_for_pasta if word == '파스타면' else 1.0
            embedding.append(model[word] * weight)
    if len(embedding) == 0:
        return np.zeros(model.vector_size)  # Return zero vector if no word in the model
    return np.mean(embedding, axis=0)  # Take the mean of weighted word embeddings

weight_for_pasta = 2.0
# Embed all recipes
embedded_recipes = [embed_recipe_with_weights(recipe, word2vec_model.wv, weight_for_pasta) for recipe in recipes]

# Calculate cosine similarity
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

# Embed your ingredient
my_ingredient = ['파스타면', '올리브유', '파슬리', '치즈', '우유']  # 임베딩을 위해 재료를 단어 단위로 분할
my_vector = embed_recipe_with_weights(my_ingredient, word2vec_model.wv, weight_for_pasta)

# Calculate similarity between your ingredient and all recipes
similarities = [cosine_similarity(my_vector, embedded_recipe) for embedded_recipe in embedded_recipes]

# Find the most similar recipe
most_similar_indices = np.argsort(similarities)[::-1][:5]  # 유사도가 높은 순서대로 상위 5개 인덱스 선택
print("Most similar recipes (top 5):")
for index in most_similar_indices:
    print(recipes[index])