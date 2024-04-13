import numpy as np
from scipy.sparse.linalg import svds

# 사용자 데이터 생성 (예제를 위해 임의로 생성)
# 사용자 나이, 음식에 대한 선호도, 성별 (0: 여성, 1: 남성)
users_data = np.array([
    [25, 5, 4, 3, 1, 0],  # 사용자 0
    [30, 3, 2, 5, 4, 1],  # 사용자 1
    [20, 4, 3, 2, 5, 1],  # 사용자 2
    [35, 2, 5, 1, 3, 0],  # 사용자 3
    [28, 5, 4, 3, 2, 1]   # 사용자 4
])

# SVD를 위해 사용자 데이터를 행렬로 변환
ratings = users_data[:, 1:-1].astype(float)  # 나이와 성별을 제외한 선호도 데이터
user_ids = users_data[:, 0]  # 사용자 ID

# SVD 적용
U, sigma, Vt = svds(ratings, k=2)  # k는 사용자 특성의 개수, 여기서는 임의로 2로 설정

# 대각 행렬로 변환
sigma = np.diag(sigma)

# 사용자의 특성을 통해 예측을 생성
predicted_ratings = np.dot(np.dot(U, sigma), Vt)

# 새로운 사용자 데이터 생성
new_user = np.array([22, 5, 3, 4, 2])  # 나이, 음식에 대한 선호도, 성별

new_user_feature = np.dot(new_user[1:], Vt.T)



# 기존 사용자 중 새로운 사용자와 가장 비슷한 사용자 찾기
similar_user_index = np.argmax(np.dot(U, new_user_feature.T))

# 결과 출력
print("새로운 사용자의 특성:", new_user_feature)
print("가장 비슷한 사용자의 인덱스:", similar_user_index)
print("가장 비슷한 사용자의 ID:", user_ids[similar_user_index])
