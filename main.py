import sqlite3
from faker import Faker

fake = Faker()

# get data from Faker library
names = [fake.name().split() for i in range(100)]

# clean the data
names = [name for name in names if len(name) == 2]

# create database and table if it doesn't already

connection = sqlite3.connect("names.db")
table = "CREATE TABLE IF NOT EXISTS people (id integer primary key, firstname TEXT, lastname TEXT)"
cursor = connection.cursor()
cursor.execute(table)

# (C) add data into database table
insert_query = "INSERT INTO people (firstname, lastname) VALUES (?, ?)"
for name in names:
    cursor.execute(insert_query, name)
connection.commit()

# (R)retrieve data
cursor.execute("SELECT * FROM people WHERE lastname LIKE 'A%'")
results = cursor.fetchall()
for row in results:
    print(row)

# (U) Update data
cursor.execute("UPDATE people SET lastname = 'Fake_lastname' WHERE lastname LIKE 'A%'")
# Commit the changes
connection.commit()

# Check if the data has been updated
cursor.execute("SELECT * FROM people WHERE lastname LIKE 'Fake_lastname%'")
results = cursor.fetchall()
for row in results:
    print(row)

# (D) Delete data
# Delete the last 10 entries in the people table after people table has been ordered by lastname
cursor.execute("DELETE FROM people ORDER BY lastname ASC LIMIT 10;")
connection.commit()

connection.close()
