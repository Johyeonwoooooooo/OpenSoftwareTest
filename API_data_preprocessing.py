#-- coding: utf-8 --
import requests
import json
 
def request_data():
    apikey = ''
    request_url = f'https://openapi.foodsafetykorea.go.kr/api/{apikey}/COOKRCP01/json/1/1000'
    response = requests.get(request_url)
    data =response.json()
    
    recipe_names = [item['RCP_NM'] for item in data['COOKRCP01']['row']]
    recipe_ingredients = [item['RCP_PARTS_DTLS'].replace('●', '').replace('-', '').replace('•', '') for item in data['COOKRCP01']['row']]
    return recipe_names, recipe_ingredients

recipe_name, recipe_ingredient = request_data()

# print(recipe_name)
#print(recipe_ingredient[0])

with open('recipe_ingredients.txt', 'w', encoding='utf-8') as file:
    json.dump(recipe_ingredient, file, ensure_ascii=False, indent=4)