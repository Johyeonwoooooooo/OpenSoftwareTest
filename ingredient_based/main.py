import pickle
import sys
sys.path.append('c:/OpenSoftware_test/collaborative_filttering')
import sys
sys.path.append('c:/OpenSoftware_test/ingredient_based')
import re
from modelByIngredient import IBRM 
from UserBased import UBRM
from gensim.models import Word2Vec

user_recommend_model = UBRM()

with open('user_based_recommend_model.pkl', 'wb') as file:
    pickle.dump(user_recommend_model, file)

