import pymysql

connection = pymysql.connect(host='localhost', user='root',password='',db='test')

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        result = cursor.fetchall()
        #print(result)
        for row in result:
            print("First Name:",row[1],"\nLast Name:",row[2],"\nemail:",row[4],"\n\n")
    connection.commit()

finally:
    connection.close()
