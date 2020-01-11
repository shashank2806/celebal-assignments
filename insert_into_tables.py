import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  passwd="passwd",
  database="db1"
)

mycursor = mydb.cursor()


# TABLE 1
mycursor.execute("TRUNCATE table data1")

df1 = pd.read_csv('dataset1.csv')
sql = "INSERT INTO data1 (ID,Cities,Pincode,Office_ID) VALUES (%s, %s, %s, %s)"
val = []
for i in range(len(df1)):
  row = df1.loc[i]
  val.append((int(row.ID), row.Cities, int(row.Pincode), row.Office_ID))
mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")


# TABLE 2
mycursor.execute("TRUNCATE table data2")

df2 = pd.read_csv('dataset2.csv')
sql = "INSERT INTO data2 (ID,Office_ID,Population) VALUES (%s, %s, %s)"
val = []
for i in range(len(df2)):
  row = df2.loc[i]
  val.append((int(row.ID), row.Office_ID, int(row.Population)))
mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")

