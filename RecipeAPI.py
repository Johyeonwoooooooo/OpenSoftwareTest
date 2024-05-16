#-- coding: utf-8 --
import requests
import json
 
def request_data():
    apikey = '360bfc50b4154894b83c'
    request_url = f'https://openapi.foodsafetykorea.go.kr/api/{apikey}/COOKRCP01/json/1/1000'
    response = requests.get(request_url)
    data =response.json()
    
    print(data)
    recipe_name = [item['MANUAL_IMG01'].replace('\n', '\\n') for item in data['COOKRCP01']['row']]

    return recipe_name

recipe_name = request_data()
# print(recipe_name)
# print(len(recipe_name))

with open('recipe_Manual01_img.txt', 'w', encoding='utf-8') as file:
     for name in recipe_name:
         file.write(name + '\n')