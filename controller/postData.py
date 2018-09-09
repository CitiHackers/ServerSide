import math
import requests
from flask import request, jsonify, mysql

def calculateMaxPrice (I, g, N, e, C, D, r, T):
    return float(N) + float(D) + float(C) + (1 - math.pow(float(g)/(1+float(r)), 83 - float(T))) * (float(I) - 12*float(e)) / (1+float(r)-float(g))

def getParameters ():
    I = request.form.get('Annnual_Income')
    g = 0.01
    N = request.form.get('Personal_Saving')
    e = float(I) * 0.5
    C = request.form.get('CPF_Saving')
    D = request.form.get('Insurance')
    r = 0.5
    T = request.form.get('Current_Age')
    location = request.form.get('location')
    maxPrice = calculateMaxPrice (I, g, N, e, C, D, r, T)
    return maxPrice, location

def listData (maxPrice, location):
    cur = mysql.connect().cursor()
    latitude = location(0);
    logitude = location(1);
    query = "SELECT H.NAME, H.PRICE FROM CITI.HOUSE AS H WHERE H.PRICE <= %s AND H.LATITUDE = %s AND H.LONGITUDE = %s ORDERED BY H.PRICE DESCENDING" % (maxPrice, latitude, logitude)
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()
    return jsonify({'properties': r})

def post ():
    maxPrice, location = getParameters()
    data = listData(maxPrice, location)
    url = 'http://localhost:8000/'
    headers = {'Content-type': 'text/html; charset=UTF-8'}
    response = requests.post(url, data=data, headers=headers)

