import math
from flask import request, jsonify


def calculate_max_price(i, g, n, e, c, d, r, t):
    return n + d + c + (1 - math.pow(g/(1+r), 50 - t)) * (i - 12.0 * e) / (1.0 + r-g)


def get_parameters():
    i = request.json.get('annualIncome')
    g = 0.1    # Singapore CPI
    n = request.json.get('personalSaving')
    e = request.json.get('monthlyExpense')
    c = request.json.get('cpfSavings')
    d = request.json.get('housingGrants')
    r = 0.02  # current risk interest rate
    t = request.json.get('currentAge')
    location = request.form.get('selectedLocation')
    max_price = calculate_max_price(float(i), g, float(n), float(e), float(c), float(d), r, float(t))
    return max_price, location


def list_data (max_price, location, cursor):
    latitude = location(0)
    longitude = location(1)
    query = "SELECT H.NAME, H.PRICE FROM CITI.HOUSE AS H WHERE H.PRICE <= %f AND H.LATITUDE <= %f + 1 AND H.LATITUDE >= %f - 1 AND H.LONGITUDE >= %f - 1 AND H.LONGITUDE <= %f + 1" % (max_price, latitude, latitude, longitude, longitude)
    cursor.execute(query)
    r = [dict((cursor.description[i][0], value)
              for i, value in enumerate(row)) for row in cursor.fetchall()]
    cursor.close()
    return jsonify({'properties': r})

