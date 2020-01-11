import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  passwd="passwd",
  database="db1"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 
