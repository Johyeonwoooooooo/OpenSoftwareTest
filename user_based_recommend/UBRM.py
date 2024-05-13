# UBRM.py

import numpy as np

users_data = [
    {"age": 25, "gender": 1, "preference": [1, 2, 5, 4, 3]},
    {"age": 30, "gender": 0, "preference": [1, 2, 3, 4, 5]},
    {"age": 35, "gender": 1, "preference": [5, 4, 5, 3, 2]},
    {"age": 40, "gender": 0, "preference": [2, 3, 4, 5, 1]},
    {"age": 45, "gender": 1, "preference": [4, 5, 1, 2, 3]}
]

def similarity(user1, user2):
    age_diff = abs(user1["age"] - user2["age"])
    gender_diff = 0 if user1["gender"] == user2["gender"] else 1
    preference_diff = np.linalg.norm(np.array(user1["preference"]) - np.array(user2["preference"]))
    return age_diff + gender_diff + preference_diff

def recommend(target_user, users_data):
    min_similarity = float('inf')
    most_similar_user = None
    
    for user in users_data:
        if user == target_user:
            continue
        sim = similarity(target_user, user)
        if sim < min_similarity:
            min_similarity = sim
            most_similar_user = user
    
    print("Most similar user:", most_similar_user)
    print("Similarity score:", min_similarity)
    
    recommended_item = max(most_similar_user["preference"], key=target_user["preference"].count)
    
    return recommended_item

target_user = {"age": 32, "gender": 1, "preference": [3, 4, 2, 5, 1]}
recommended_item = recommend(target_user, users_data)
print("Recommended item:", recommended_item)

