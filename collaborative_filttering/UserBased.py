# UBRM.py
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
import pymysql

class UBRM:
    def __init__(self):
        self.standardizer =  StandardScaler()
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.db = 'still88'
        self.recipe_num = 998
        
    def read_userInfo(self):
        conn = pymysql.connect(host=self.host, user=self.user
                                  ,password=self.password, db=self.db, charset='utf8')
        cursor = conn.cursor()
        cursor.execute(f"SELECT userAge, userGender, userFavorite from User;")

        result = cursor.fetchall()

        user_info_list = []
        for row in result:
            user_info = [row[0], row[1], row[2].split(',')]
            user_info_list.append(user_info)
        cursor.close()
        conn.close()

        return user_info_list
    
    def normalize_age(self, user_info):
        ages = [user[0] for user in user_info]
        normalized_ages = self.standardizer.fit_transform([[age] for age in ages])

        for i, user in enumerate(user_info):
            user_info[i][0] = normalized_ages[i][0]
        
        return user_info


    def transformUserInfoToVector(self, user_info):
        rows = []
        cols = []
        data = []
        additional_features = [] 
        recipe_count = self.recipe_num

        for i, (age, gender, recipes) in enumerate(user_info):
            for recipe in recipes:
                rows.append(i)
                cols.append(recipe) 
                data.append(1)
            additional_features.append([age, 1 if gender == True else 0])

        user_recipe_matrix = csr_matrix((data, (rows, cols)), shape=(len(user_info), recipe_count))

        additional_features = np.array(additional_features)
        user_features_matrix = np.hstack((additional_features, user_recipe_matrix.toarray()))

        return user_features_matrix

    def recommend(self, userId):
        user_info = self.read_userInfo()
        user_info = self.normalize_age(user_info)
        user_vector = self.transformUserInfoToVector(user_info)

        cosine_sim = cosine_similarity(user_vector)[userId]
        cosine_sim[userId] = -1

        most_similar_users = np.argsort(cosine_sim)[-5:][::-1]

        conn = pymysql.connect(host=self.host, user=self.user
                                  ,password=self.password, db=self.db, charset='utf8')
        
        cursor = conn.cursor()

        recipe_score_sum = np.zeros(998)

        for userId in most_similar_users:
            cursor.execute(f"SELECT userFavorite FROM User WHERE userId = {userId};")
            result = cursor.fetchone()
            if result:
                favorite_recipes = [int(r) for r in result[0].split(',')]
                user_favorite_vector = np.zeros(998)
                user_favorite_vector[favorite_recipes] = 1
                recipe_score_sum += user_favorite_vector

        recipe_score_average = recipe_score_sum / 5

        cursor.close()
        conn.close()

        return recipe_score_average