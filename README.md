# Flask MVC Structure

pip install Flask-MySQLdb

# ---------------------[ MySQL Database ]---------------------

from flask_mysqldb import MySQL

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "01252"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_DB"] = "book_store"

# Connection
mysql = MySQL(app)

@app.route("/books")
def users():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM books""")
    rv = cur.fetchall()
    return str(rv)

# ---------------------[ MySQL Database ]---------------------

pip install mysql-connector-python

# ---------------------[ MySQL Database ]---------------------

import mysql.connector

mysql = mysql.connector.connect(
    user='root',
    password='01252',
    host='localhost',
    database='book_store'
)

con = mysql.connector.connect()
cur = con.cursor()

con.close()

# ---------------------[ MySQL Database ]---------------------