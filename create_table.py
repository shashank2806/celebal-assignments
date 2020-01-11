import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  passwd="passwd",
  database="db1"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE data1 (ID INTEGER, Cities VARCHAR(255), Pincode INTEGER, Office_ID VARCHAR(255))")
# mycursor.execute("CREATE TABLE data2 (ID INTEGER, Office_ID VARCHAR(255), Population INTEGER)");

mycursor.execute("CREATE TABLE merged_data (ID INTEGER, Cities VARCHAR(255), Pincode INTEGER, Office_ID VARCHAR(255), Population INTEGER)")
