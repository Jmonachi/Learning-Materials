import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root@localhost",
  password="",
)

print(mydb)

mycursor = mydb.cursor()