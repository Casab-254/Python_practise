import psycopg2
try:
  conn=psycopg2.connect(database="brad", user="postgres" , password="@Kenya254" , host="127.0.0.1" , port="5432")
  print("Database connected successfully")
except:
  print("Error occured when connecting to the database")

cur = conn.cursor()
def create_table():
  cur.execute("create table test (id INT, Name varchar(100), email varchar(100));")
  conn.commit()

create_table()
cur = conn.cursor()
def create_table():
  cur.execute("create table test (id INT, Name varchar(100), email varchar(100));")
  conn.commit()

# create_table()

def insert_record():
    cur.execute("Insert into test values(1, 'Bradley', 'softcoding254.com')")
conn.commit()
insert_record()


def view_records():
   cur.execute("select * from test;")
   tests= cur.fetchall()
   print(tests)

view_records()