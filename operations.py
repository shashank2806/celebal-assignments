import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    passwd="passwd",
    database="db1"
)


# Join
mycursor = mydb.cursor()

sql = "SELECT data1.ID, data1.Cities,data1.Pincode,data1.Office_ID, data2.Population\
  FROM data1 \
  INNER JOIN data2 ON data1.Office_ID = data2.Office_ID"

mycursor.execute(sql)

myresult = mycursor.fetchall()


# Save result to a new table after join
mycursor.execute("TRUNCATE table merged_data")
sql2 = "INSERT INTO merged_data (ID,Cities,Pincode,Office_ID, Population) VALUES (%s, %s, %s, %s, %s)"
val = []
for x in myresult:
    val.append(x)
mycursor.executemany(sql2, val)

mydb.commit()

# Groupby Pincode
mycursor.execute(
    "select Pincode, SUM(Population) FROM merged_data WHERE Cities='Jaipur' GROUP BY Pincode")
myresult = mycursor.fetchall()
# for x in myresult:
#     print(x[0], x[1])

with open('result.txt', 'w') as f:
    for x in myresult:
        f.write(f'{x[0]}: {x[1]} \n')
