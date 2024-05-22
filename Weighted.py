import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dot, Dense

# 하이퍼파라미터 설정
num_users = 100  # 사용자 수
num_recipes = 1000  # 레시피 수
embedding_size = 50  # 임베딩 차원

# 모델 구축
user_input = Input(shape=(1,))
recipe_input = Input(shape=(1,))

user_embedding = Embedding(num_users, embedding_size)(user_input)
recipe_embedding = Embedding(num_recipes, embedding_size)(recipe_input)

user_vector = Flatten()(user_embedding)
recipe_vector = Flatten()(recipe_embedding)

dot_product = Dot(axes=1)([user_vector, recipe_vector])

# 피드백을 반영한 Dense 층 추가
dense = Dense(128, activation='relu')(dot_product)
output = Dense(1, activation='sigmoid')(dense)

model = Model(inputs=[user_input, recipe_input], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 데이터 준비 (샘플 데이터)
user_ids = np.random.randint(0, num_users, size=1000)
recipe_ids = np.random.randint(0, num_recipes, size=1000)
ratings = np.random.randint(0, 2, size=1000)  # 피드백 (0 또는 1)

# 모델 학습
model.fit([user_ids, recipe_ids], ratings, epochs=10, batch_size=64)

# 예측
predictions = model.predict([user_ids, recipe_ids])
print(predictions[9])