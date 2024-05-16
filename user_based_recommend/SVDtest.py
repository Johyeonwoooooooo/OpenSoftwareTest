from sklearn.decomposition import TruncatedSVD
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

userData = [
    [0.25, 1],
    [0.75, 0, 3],
    [0.5, 1, 2, 10, 2, 5, 7],
    [0.6, 0, 3, 2, 1, 4, 4]
]

max_length = max(len(sub_array) for sub_array in userData)

padded_data = [sub_array + [0] * (max_length - len(sub_array)) for sub_array in userData]

userData_np = np.array(padded_data)

svd = TruncatedSVD(n_components=3)
svd.fit(userData_np)
transformed_data = svd.transform(userData_np)

#print(transformed_data)


similarity_matrix = cosine_similarity(transformed_data)

print(similarity_matrix)

for i in range(len(userData)):
    # Exclude the current user's index from comparison
    mask = np.ones(len(similarity_matrix), dtype=bool)
    mask[i] = False

    # Apply the mask to filter out the current user
    filtered_similarities = similarity_matrix[i][mask]

    # Find the index of the most similar user, adjusting for the removed index
    most_similar_user = np.argmax(filtered_similarities)
    if most_similar_user >= i:
        most_similar_user += 1  # Adjust index since we removed i-th user
    
    print(f"User {i+1} is most similar to User {most_similar_user + 1}")
