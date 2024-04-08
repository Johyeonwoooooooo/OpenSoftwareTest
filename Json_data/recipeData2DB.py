#-- coding: utf-8 --
'''
python to DB (mysql)

pip install pymysql
'''

# import requests
# import json
# import pymysql
 
# def request_data():
#     apikey = '360bfc50b4154894b83c'
#     request_url = f'https://openapi.foodsafetykorea.go.kr/api/{apikey}/COOKRCP01/json/1/1000'
#     response = requests.get(request_url)
#     data =response.json()
    
#     recipe_names = [item['RCP_NM'] for item in data['COOKRCP01']['row']]
#     recipe_ingredients = [item['RCP_PARTS_DTLS'].replace('?óè', '').replace('-', '').replace('???', '')
#                           .replace('Ï£ºÏû¨Î£? : ', '').replace('?ïÑ?àò ?û¨Î£? : ', '').replace('?û¨Î£? ','')
#                           .replace('[ 2?ù∏Î∂? ] ', '') for item in data['COOKRCP01']['row']]
#     return recipe_names, recipe_ingredients

# recipe_name, ingredient_list = request_data()

# conn = pymysql.connect(host='127.0.0.1', user='root', password='zpalq,123098!@#', db='ossp', charset='utf8')
# cur = conn.cursor()

# for ingredient in ingredient_list:
#     cur.execute("INSERT INTO ingredient (ingredient) VALUES (%s)", (ingredient))
#     conn.commit()

# print('commit success')

import pymysql

file_path = 'C:\\OpenSoftware_test\\Json_data\\recipe_ingredients.txt'
conn = pymysql.connect(host='localhost', user='root', password='zpalq,123098!@#', db='ossp', charset='utf8')
cur = conn.cursor()

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip() != '[' or line.strip() != ']':
            cur.execute("INSERT INTO ingredient (ingredient) VALUES (%s)", (line.strip()))
            conn.commit()