#-- coding: utf-8 --
import requests
import json
 
def request_data():
    apikey = '360bfc50b4154894b83c'
    request_url = f'https://openapi.foodsafetykorea.go.kr/api/{apikey}/COOKRCP01/json/1/1000'
    response = requests.get(request_url)
    data =response.json()
    
    recipe_name = [item['RCP_NM'] for item in data['COOKRCP01']['row']]

    return recipe_name

recipe_category = request_data()
print(recipe_category)

# with open('recipe_name.txt', 'w', encoding='utf-8') as file:
#     for category in recipe_category:
#         file.write(category + '\n')