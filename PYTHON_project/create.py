import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!@#$%^&*()",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)