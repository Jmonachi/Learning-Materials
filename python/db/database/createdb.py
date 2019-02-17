import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="YES"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")