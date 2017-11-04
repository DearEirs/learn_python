#!/bin/env python
#!encode:utf-8

from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def handle():
    title = request.args.get('title')
    page = request.args.get('page')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from table where title='" + title + "' and page='" +
                   page + "'")
    data = cursor.fetchall()
    return data

if __name__ == "__main__":
    app.run()
