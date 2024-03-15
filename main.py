import psycopg2
from flask import Flask, render_template

conn = psycopg2.connect(user="postgres", password="@Kenya254",host="127.0.0.1", port="5432", database="sales_management")
cur=conn.cursor()
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY,name VARCHAR(100),buying_price INT,selling_price INT,stock_quantity INT);")
cur.execute("CREATE TABLE IF NOT EXISTS sales (id serial PRIMARY KEY,pid INT, quantity INT, created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW() );")
conn.commit()
app = Flask(__name__)


@app.route("/")
def index():
    return render_templates("inedx.html")

app.run()