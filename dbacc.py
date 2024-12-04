# Module Imports
import mariadb
import sys
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="0000",
        host="localhost",
        port=3306,
        database="mydb"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

conn.autocommit = True
#----------------------------------------------

# Get Cursor
cur = conn.cursor()
# selectall = "SELECT * from mytable02" 
select_all_query = "SELECT id, name, age from mytable02" 
cur.execute( select_all_query )

# query 결과를 list 형으로 가져옴.
resultset = cur.fetchall()

print('-------- select all data ----------')
for id, name, age in resultset: 
    print(f"id: {id}, name: {name}, age: {age}")

#----------------------------------------------

some_name = "홍길동" 
select_where_query = "SELECT id, name, age from mytable02 WHERE name=?" 

cur.execute( select_where_query,(some_name,))
resultset = cur.fetchall()

print('-------- select 홍길동 data ----------')
for id, name, age in resultset: 
    print(f"id: {id}, name: {name}, age: {age}")

#----------------------------------------------

another_name = "임신중"
another_age = 28

insert_query = "INSERT INTO mytable02 (name, age) VALUES (?, ?)"

try: 
    cur.execute( insert_query, (another_name, another_age))
except mariadb.Error as e: 
    print(f"Error: {e}")

#Re print ----------------------------------------------

cur.execute( select_all_query )

# query 결과를 list 형으로 가져옴.
resultset = cur.fetchall()

print('-------- select all data ----------')
for id, name, age in resultset: 
    print(f"id: {id}, name: {name}, age: {age}")

#--------------------------------
conn.close()