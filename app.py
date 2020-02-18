#!flask/bin/python
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def db_query():
    config = {
        'user': 'root',
        'password': 'zxc',
        'host': 'db-srv',
        'port': '3306',
        'database': 'weather'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM city_temp')
    results = [{'sl': no, 'city': city, 'temp': temp} for (no, city, temp) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/api/v01/all')
def index():
    return json.dumps(db_query())
    #return json.dumps({'city_temp': db_query()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)




