import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/some_data', methods=['GET'])
def get_scanner_data():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {33489} ( latest volume >= 100000 and latest close >= 50 and latest close >= latest ema( latest close , 21 ) and latest close >= 1 day ago close and latest close - 1 candle ago close / 1 candle ago close * 100 <= 5 and( latest high - latest close ) / ( latest high - latest low ) <= 0.5 and latest ema( latest close , 9 ) >= latest ema( latest close , 21 ) ) )  "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

if __name__ == '__main__':
    app.run()

