import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (name, address) VALUES (%s, %s)"
val = [
  ('Brian', 'Nairoi 1'),
  ('Sarah', 'Kwapole'),
  ('Agrey', 'Leganga'),
  ('Bahati', 'Usa River')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, " data were inserted.")