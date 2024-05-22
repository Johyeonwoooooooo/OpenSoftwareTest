import pymysql
import json

def read_ingredients(file_path, encodings=['utf-8']):
    ingredients = []
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                for line in file:
                    ingredients.append(line.strip())
            return ingredients
        except UnicodeDecodeError:
            continue  # Try next encoding
        except FileNotFoundError:
            print(f"Error: The file {file_path} does not exist.")
            return []
    print(f"Error: Could not decode file {file_path} with given encodings.")
    return []

# 경로 변경
file_path = "C:\\Users\\HYEONWOO\\Desktop\\recipe\\recipe_name.txt"
recipe_name = read_ingredients(file_path)

file_path2 = "C:\\Users\\HYEONWOO\\Desktop\\recipe\\recipe_category.txt "
recipe_category = read_ingredients(file_path2)

file_path3 = "C:\\OpenSoftware_test\\Json_data\\recipe_ingredients.txt"
recipe_ingredients = read_ingredients(file_path3)

if len(recipe_name) != len(recipe_category):
    print("Error: The number of ingredients does not match the number of categories.")
    print(len(recipe_ingredients))
    print(len(recipe_category))
    print(len(recipe_name))
else:
    try:
        conn = pymysql.connect(host='localhost', user='root', password='zpalq,123098!@#', db='still88', charset='utf8')
        cursor = conn.cursor()

        for i in range(len(recipe_name)):
            recipe_ingredient = recipe_ingredients[i].split(' ')[::2]
            # Convert the list to a JSON string
            ingredient_json = json.dumps(recipe_ingredient)
            query = "INSERT INTO recipe(recipeName, recipeCategory, recipeIngredient) VALUES (%s, %s, %s);"
            cursor.execute(query, (recipe_name[i], recipe_category[i], ingredient_json))

        conn.commit()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
