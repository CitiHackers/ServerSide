from flask import Flask
from flaskext.mysql import MySQL
import requests
from controller import postData
from controller import sortList

app = Flask(__name__)
mysql = MySQL()


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'citi'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

with mysql.connect().cursor() as cursor:
    cursor.execute(open("DB_script/schema.sql", "r").read())


@app.route('/post_data', methods=['GET', 'POST'])
def post():
    max_price, location = postData.get_parameters()
    data = postData.list_data(max_price, location, cursor)
    sorted_data = sortList.sort_property_list(data, location)
    url = 'http://localhost:8000/'
    headers = {'Content-type': 'text/html; charset=UTF-8'}
    requests.post(url, data=sorted_data, headers=headers)
    return sorted_data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)