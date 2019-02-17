import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="",
  passwd=""
)

print(mydb)