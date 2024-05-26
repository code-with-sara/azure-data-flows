from flask import Flask, render_template, request

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sara1234'
app.config['MYSQL_DB'] = 'tutorial'

mysql = MySQL(app)
@app.route('/', methods = ['GET', 'POST'])


def file():
    

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        cur = mysql.connection.cursor()
        cur.execute("insert into user (name, email) values(%s, %s)" ,(name, email))
        
        mysql.connection.commit()
        cur.close()
        
        return "Oh Added Successfully" 
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)