import mysql.connector

cnx = mysql.connector.connect(user='student', password='aLQQLXGQp2rJ4Wy5',
                              host='173.246.108.142',
                              database='Project_169',
                              port='3306')
cursor = cnx.cursor()

query = ("SELECT name FROM TVShow ORDER BY name")

cursor.execute(query)

cursor.close()
cnx.close()
