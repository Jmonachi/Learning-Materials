import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers WHERE name = 'amy' ")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)