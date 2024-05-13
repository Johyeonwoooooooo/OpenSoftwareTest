from surprise import Dataset, Reader

# 데이터셋 정의
data = [
    (20, 0, [2, 3, 5, 10, 12, 25]),
    (15, 0, [2, 10 ,23 , 50]),
    (40, 1, [0, 5, 20, 25])
]

# Surprise에서 사용할 데이터 포맷 정의
reader = Reader(rating_scale=(0, 1))

# Surprise 데이터셋 생성
dataset = Dataset.load_from_df([(u, i, 1) for u, _, items in data for i in items], reader)

# 전체 데이터셋으로 학습
trainset = dataset.build_full_trainset()

# KNN 알고리즘 선택 (이 예제에서는 아이템 기반 협업 필터링을 사용)
sim_options = {'name': 'cosine', 'user_based': False}
model = KNNBasic(sim_options=sim_options)

# 모델 학습
model.fit(trainset)

# 주어진 사용자의 ID
target_user_id = 0  # 예시로 첫 번째 사용자를 선택

# 주어진 사용자와 유사한 사용자들을 찾기
similarity = model.get_neighbors(target_user_id, k=3)  # 상위 3개의 유사한 사용자

print("Target User ID:", target_user_id)
print("Similar Users:", similarity)
