import pymysql

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
file_path = "C:\\Users\\HYEONWOO\\Desktop\\recipe\\ingredientList.txt"
ingredient_name = read_ingredients(file_path)

file_path2 = "C:\\Users\\HYEONWOO\\Desktop\\recipe\\ingredientCategory.txt"
ingredient_category = read_ingredients(file_path2)

if len(ingredient_name) != len(ingredient_category):
    print("Error: The number of ingredients does not match the number of categories.")
else:
    try:
        conn = pymysql.connect(host='localhost', user='root', password='zpalq,123098!@#', db='still88', charset='utf8')
        cursor = conn.cursor()

        for i in range(len(ingredient_name)):
            query = "INSERT INTO ingredient(ingredientCategory, ingredientName) VALUES (%s, %s);"
            cursor.execute(query, (ingredient_category[i], ingredient_name[i]))

        conn.commit()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
