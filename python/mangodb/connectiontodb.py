import mysql.connector

mon = mysql.connector.connect(
  host="localhost",
  user="root'@'127.0.0.1",
  passwd="password123"
)

print(mon)