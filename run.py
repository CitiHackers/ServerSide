from flask import Flask, jsonify
from flaskext.mysql import MySQL
import requests
from controller import postData

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'citi'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/postData', methods=['GET', 'POST'])
def post():
    maxPrice, location = postData.getParameters()
    data = postData.listData(maxPrice, location)
    url = 'http://localhost:8000/'
    headers = {'Content-type': 'text/html; charset=UTF-8'}
    requests.post(url, data=data, headers=headers)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)