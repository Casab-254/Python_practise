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