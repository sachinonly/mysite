import mysql.connector
con = mysql.connector.connect(
    user = "root",
    password = "Mysql123#",
    host = "localhost",
    database = "world"
)

cursor = con.cursor()


query = cursor.execute("SELECT * FROM city")
results = cursor.fetchall()
print(results)
