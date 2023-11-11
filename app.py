import pandas as pd
import  Config
import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/LongStockOneDayAgo', methods=['GET'])
def get_long_scanner_data():
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

@app.route('/api/ShortStockOneDayAgo', methods=['GET'])
def get_short__scanner_data():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {33489} ( latest volume >= 100000 and latest close >= 50 and latest close <= latest ema( latest close , 21 ) and latest close <= 1 day ago close and latest close - 1 candle ago close / 1 candle ago close * 100 >= -5 and( latest close - latest low ) / ( latest high - latest low ) <= 0.5 and latest ema( latest close , 9 ) <= latest ema( latest close , 21 ) ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/LongStockLiveIntraday', methods=['GET'])
def get_long_intraday_stock_scanner_data():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {33489} ( latest volume > 10000 and latest close > 50 and 1 day ago close - 1 candle ago close / 1 candle ago close * 100 < 5 and latest high / latest close <= 1.003 and latest close >= 1 day ago high and( [0] 5 minute sma( [0] 5 minute volume , 4 ) - latest sma( 2 days ago volume / 75 , 5 ) ) / 2 days ago sma( latest volume , 75 ) * 100 > 0 and( {33489} ( [0] 5 minute close - [0] 5 minute open / [0] 5 minute open * 100 < 0.05 or [-1] 5 minute close - [-1] 5 minute open / [-1] 5 minute open * 100 < 0.05 or [-2] 5 minute close - [-2] 5 minute open / [-2] 5 minute open * 100 < 0.05 ) ) ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/SwingStockScanner', methods=['GET'])
def swing_scanner_data():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {cash} ( latest close >= 30 and latest close >= 1 day ago close and latest close >= latest open and latest close >= latest ema( latest close , 200 ) and latest sma( latest close , 20 ) > latest sma( latest close , 50 ) and latest volume >= 100000 and latest volume >= latest sma( latest volume , 20 ) and latest rsi( 14 ) >= 40 ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/VolumeBreakout', methods=['GET'])
def volume_breakout_stock_data():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {33489} ( [0] 5 minute close > 15 days ago high and latest volume > 50 days ago volume ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/IntradayBoost', methods=['GET'])
def intraday_boost_stock_data():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {57960} ( latest close > latest ema( close,50 ) and latest ema( close,50 ) > latest ema( close,150 ) and latest ema( close,20 ) > latest ema( close,200 ) and [0] 15 minute volume > [0] 1 hour sma( volume,50 ) and [0] 15 minute close > 1 day ago close and latest stochrsi( 14 ) > 60 and latest volume > 30 days ago sma( volume,30 ) and latest sma( volume,120 ) > 100000 and( {57960} ( [=1] 30 minute volume > 100000 and latest high - latest low > 1 day ago close * 1.03 - 1 day ago close and [=2] 15 minute adx di positive( 14 ) > [=2] 15 minute adx di negative( 14 ) and [=2] 15 minute adx( 14 ) < [=2] 15 minute adx di positive( 14 ) and [=2] 15 minute adx( 14 ) > [=2] 15 minute adx di negative( 14 ) ) ) ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/FiftyTwoWeekHigh', methods=['GET'])
def fifty_two_week_high():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {cash} ( latest close >= 50 and latest ema( close,5 ) > latest ema( close,26 ) and latest ema( close,13 ) > latest ema( close,26 ) and latest close > 1 day ago close * 1.03 and latest volume > latest sma( volume,20 ) * 1.0 and latest ema( close,5 ) > latest ema( close,13 ) and latest high = latest max( 260 , latest high ) * 1 and 1 day ago close > 2 days ago close * 0.98 ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/PoleAndFlagStock', methods=['GET'])
def pole_and_flag_stock():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {cash} ( latest close >= 10 days ago close * 1.2 and latest close > 50 and market cap > 500 and latest sma( latest volume , 20 ) * latest close >= 10000000 ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/ATRSwingStocks', methods=['GET'])
def atr_swing_stocks():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {cash} ( latest avg true range( 14 ) < 10 days ago avg true range( 14 ) and latest avg true range( 14 ) / latest close < 0.08 and latest close > ( weekly max( 52 , weekly close ) * 0.75 ) and latest ema( latest close , 50 ) > latest ema( latest close , 150 ) and latest ema( latest close , 150 ) > latest ema( latest close , 200 ) and latest close > latest ema( latest close , 50 ) and latest close > 10 and latest close * latest volume > 1000000 and latest close - 1 candle ago close / 1 candle ago close * 100 >= 0 and( {166311} not( latest close > 0 ) ) and( {167068} not( latest close > 0 ) ) ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/DojiSwingStocks', methods=['GET'])
def doji_swing_stocks():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {cash} ( latest volume > 200000 and latest high > latest close and latest low < latest close and latest close > latest sma( close,20 ) and( {cash} ( latest open / latest close > 1 and 1 day ago  open / 1 day ago  close <= 1 or latest open / latest close < 1 and 1 day ago  open / 1 day ago  close >= 1 or latest open = latest close ) ) and latest open / latest close > 0.99 and latest close / latest open > 0.99 ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/TurtleSwingStocks', methods=['GET'])
def turtle_swing_stocks():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {cash} ( latest close >= 1 day ago max( 20 , latest high ) and 1 day ago high <= 2 days ago max( 20 , latest high ) and latest close > latest open and latest close > latest sma( latest close , 20 ) and latest sma( latest close , 20 ) > latest sma( latest close , 50 ) and latest sma( latest close , 50 ) > latest sma( latest close , 100 ) and latest volume > 500000 and latest volume > latest sma( latest volume , 20 ) and latest close > 50 and latest rsi( 14 ) >= 60 ) )  "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/RocketIntradayBullish', methods=['GET'])
def rocket_intraday_bullish():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {33489} ( [0] 15 minute close > [0] 15 minute vwap and [0] 15 minute close > [0] 15 minute ema( close,8 ) and [0] 15 minute close > [0] 15 minute sma( close,20 ) and [0] 1 hour close > [0] 1 hour sma( close,20 ) and [0] 1 hour rsi( 8 ) > 60 and [0] 1 hour macd line( 26,12,9 ) > [0] 1 hour macd signal( 26,12,9 ) and [0] 15 minute macd line( 26,12,9 ) > [0] 15 minute macd signal( 26,12,9 ) ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/RocketIntradayBearish', methods=['GET'])
def rocket_intraday_bearish():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {33489} ( [0] 15 minute close < [0] 15 minute vwap and [0] 15 minute close < [0] 15 minute ema( close,8 ) and [0] 15 minute close < [0] 15 minute sma( close,20 ) and [0] 1 hour close < [0] 1 hour sma( close,20 ) and [0] 1 hour macd line( 26,12,9 ) < [0] 1 hour macd signal( 26,12,9 ) and [0] 15 minute macd line( 26,12,9 ) < [0] 15 minute macd signal( 26,12,9 ) ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/ThirtyDaysConsolidation', methods=['GET'])
def thirty_days_consolidation():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {cash} ( latest close * 1.05 > latest max( 200 , latest high ) and latest max( 30 , latest high ) <= 30 days ago max( 200 , latest high ) and latest volume > latest sma( volume,50 ) and latest close > 90 ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/TodaysHighMoveStocks', methods=['GET'])
def todays_high_move_stocks():
    url = "https://chartink.com/screener/process"
    condition = {"scan_clause" : "( {cash} ( latest close - 1 candle ago close / 1 candle ago close * 100 >= 10 and latest close >= 10 ) ) "}
    with requests.session() as s:
        r_data = s.get(url)
        soup = bs(r_data.content, "lxml")
        meta = soup.find("meta", {"name" : "csrf-token"})["content"]
        header = {"x-csrf-token" : meta}
        data = s.post(url, headers=header, data=condition).json()
        stock_list = data["data"]
        print(stock_list)
    return jsonify(stock_list)

@app.route('/api/SendTelegramAlert/<string:bot_message>', methods=['GET'])
def telegram_bot_sendtext(bot_message):
    try:
        bot_message = bot_message.replace('&','')
        send_text = 'https://api.telegram.org/bot' + Config.BOT_TOKEN + '/sendMessage?chat_id=' + Config.Group_ID + '&parse_mode=HTML&text=' + bot_message
        res = requests.get(send_text)
        return "Msg Sent Successfully"
        #print(f'Telegram response : {res.json()}')
    except Exception as e:
        print(f'Error in sending Telegram msg {e}')
        return "Error"

if __name__ == '__main__':
    app.run()

