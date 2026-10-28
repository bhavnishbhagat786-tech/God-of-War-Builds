import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Kratos@123",
    database="gow_armors"
)

# Create cursor
cursor = conn.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM armors")

# Fetch all rows
rows = cursor.fetchall()

# Get column names
columns = [column[0] for column in cursor.description]

# Create Pandas DataFrame
df = pd.DataFrame(rows, columns=columns)

# Display first 5 rows
print(df.head())

# Display column names
print(df.columns)




'''pracrice work data exploration'''

print(df.head())  # show first few coloums and raws
print(df.tail())  # show last  few coloums and raws

print("shape", df.shape)   #total number of rowas and coloums
print("coloums : ", df.columns)   # show all coloums in table
print("info : ", df.info)   # print all rows and coloums scribe count, mean, std, min, %, max etc

'''data filtering'''

print(df[df["armor_type"] == "chest"]) # fiter all chest armors in table/dtaframe

print(df[df["defense"] > 150])

print("defense chest : ", df[df["defense"]  == "chest"])

print("defense unique : ", df["armor_type"].unique()) #filter all armor type by "chest wrist and "waist"


