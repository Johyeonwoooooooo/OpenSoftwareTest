import pymysql

conn = pymysql.connect(host='localhost', user='root', password='zpalq,123098!@#', db='still88', charset='utf8')

cursor = conn.cursor()

query = "select * from 주문;"
cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row[1])

cursor.close()
conn.close()
