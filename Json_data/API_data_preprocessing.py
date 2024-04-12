#-- coding: utf-8 --
import requests
import json
 
def request_data():
    apikey = '360bfc50b4154894b83c'
    request_url = f'https://openapi.foodsafetykorea.go.kr/api/{apikey}/COOKRCP01/json/1/1000'
    response = requests.get(request_url)
    data =response.json()
    
    #recipe_names = [item['RCP_NM'] for item in data['COOKRCP01']['row']]
    recipe_category = [item['HASH_TAG'] for item in data['COOKRCP01']['row']]
    #recipe_ingredients = []
    # recipe_ingredients = [item['RCP_PARTS_DTLS'].replace('?ï¿½ï¿½', '').replace('-', '').replace('???', '')
    #                       .replace('ì£¼ìž¬ï¿?? : ', '').replace('?ï¿½ï¿½?ï¿½ï¿½ ?ï¿½ï¿½ï¿?? : ', '').replace('?ï¿½ï¿½ï¿?? ','')
    #                       .replace('[ 2?ï¿½ï¿½ï¿?? ] ', '').replace('\n', ', ').replace(',', '') for item in data['COOKRCP01']['row']]

    return recipe_category # recipe_names, recipe_ingredients

# recipe_name, ingredient_list = request_data()

recipe_category = request_data()
print(recipe_category)