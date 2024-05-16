import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dot, Dense

# �������Ķ���� ����
num_users = 1000  # ����� ��
num_recipes = 5000  # ������ ��
embedding_size = 50  # �Ӻ��� ����

# �� ����
user_input = Input(shape=(1,))
recipe_input = Input(shape=(1,))

user_embedding = Embedding(num_users, embedding_size)(user_input)
recipe_embedding = Embedding(num_recipes, embedding_size)(recipe_input)

user_vector = Flatten()(user_embedding)
recipe_vector = Flatten()(recipe_embedding)

dot_product = Dot(axes=1)([user_vector, recipe_vector])

# �ǵ���� �ݿ��� Dense �� �߰�
dense = Dense(128, activation='relu')(dot_product)
output = Dense(1, activation='sigmoid')(dense)

model = Model(inputs=[user_input, recipe_input], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# ������ �غ� (���� ������)
user_ids = np.random.randint(0, num_users, size=10000)
recipe_ids = np.random.randint(0, num_recipes, size=10000)
ratings = np.random.randint(0, 2, size=10000)  # �ǵ�� (0 �Ǵ� 1)

# �� �н�
model.fit([user_ids, recipe_ids], ratings, epochs=10, batch_size=64)

# ����
predictions = model.predict([user_ids, recipe_ids])
