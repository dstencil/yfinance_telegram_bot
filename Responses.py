from datetime import datetime
import yfinance as yf

stocks = ['AAPL', 'MSFT', 'AMD']

def price_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in (stocks):
        msft = yf.Ticker(stocks)
        price = msft.info['regularMarketPrice']
        return(str(price))
    
    if user_message in ("aapl"):
        msft = yf.Ticker("AAPL")
        price = msft.info['regularMarketPrice']
        return(str(price))

    if user_message in ("msft"):
        msft = yf.Ticker("MSFT")
        price = msft.info['regularMarketPrice']
        return(str(price))
    
     
    if user_message in ("amd"):
        msft = yf.Ticker("AMD")
        price = msft.info['regularMarketPrice']
        return(str(price))
   
    return "I dont understand..."
