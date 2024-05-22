from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 사용자 정보와 레시피 좋아요 정보
# 예: "사용자 ID": ([레시피 인덱스 리스트], 성별, 나이)
user_info = {
    "User A": ([1, 3], 0, 25),
    "User B": ([0, 2], 1, 30),
    "User C": ([2, 3, 4], 1, 22),
    "User D": ([3, 4], 0, 35),
}

# 나이 정규화 함수
def normalize_age(age):
    min_age = 18
    max_age = 60
    return (age - min_age) / (max_age - min_age)

# 사용자별 특성 벡터 생성
rows = []
cols = []
data = []
additional_features = []  # 성별과 정규화된 나이를 저장할 리스트

recipe_count = 1000  # 레시피 개수
for i, (user, (recipes, gender, age)) in enumerate(user_info.items()):
    for recipe in recipes:
        rows.append(i)
        cols.append(recipe)
        data.append(1)
    additional_features.append([normalize_age(age), gender])

# 희소 행렬 생성
user_recipe_matrix = csr_matrix((data, (rows, cols)), shape=(len(user_info), recipe_count))

# 추가 특성(성별, 나이)을 넘파이 배열로 변환 후 희소 행렬과 결합
additional_features = np.array(additional_features)
user_features_matrix = np.hstack((additional_features, user_recipe_matrix.toarray()))

print(user_features_matrix)
# 코사인 유사도 계산
cosine_sim = cosine_similarity(user_features_matrix)

print("Cosine Similarity:")
print(cosine_sim)
