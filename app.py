from flask import Flask, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
import os

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/EcoParameters_db"
mongo = PyMongo(app)



@app.route("/")
def welcome():
    return (
        f"Question: How are stock prices affected by market conditions such as gross domestic product (GDP), consumer price index (CPI) and unemployment rates?<br>"
        f"Data Sources:<br/>"
        f"Federal Reserve Economic Data<br/>"
        f"Yahoo Finance<br>"
        f"NASDAQ<br>"
        f"This application contains the following APIs<br>" 
        f"/stock/Energy/ticker<br>"
        f"/stock/Healthcare/ticker<br>"
        f"/stock/Technology/ticker<br>"
        f"/stock/Finance/ticker<br>"
        f"/CPI<br>"
        f"/GDP<br>"
        f"/Unemployment_rate<br>"
    )

@app.route("/stock/Energy/<co_ticker>")

def stock_prices_energy(co_ticker):
    stock_info = mongo.db.StockPrice_Energy.find({"Ticker":co_ticker})
    l = list(stock_info)
    return dumps(l)

@app.route("/stock/Healthcare/<co_ticker>")
def stock_prices_health(co_ticker):
    stock_info = mongo.db.StockPrice_Healthcare.find({"Ticker":co_ticker})
    l = list(stock_info)
    return dumps(l)

@app.route("/stock/Finance/<co_ticker>")
def stock_prices_finance(co_ticker):
    stock_info = mongo.db.StockPrice_Finance.find({"Ticker":co_ticker})
    l = list(stock_info)
    return dumps(l)

@app.route("/stock/Technology/<co_ticker>")
def stock_prices_tech(co_ticker):
    stock_info = mongo.db.StockPrice_Technology.find({"Ticker":co_ticker})
    l = list(stock_info)
    return dumps(l)

@app.route("/GDP")
def gdp():
    stock_info = mongo.db.GDP.find()
    l = list(stock_info)
    return dumps(l)

@app.route("/CPI")
def cpi():
    stock_info = mongo.db.CPI.find()
    l = list(stock_info)
    return dumps(l)

@app.route("/Unemployment_rate")
def jobs():
    stock_info = mongo.db.Unemployment_rate.find()
    l = list(stock_info)
    return dumps(l)

if __name__ == "__main__":
    app.run(debug=True)
