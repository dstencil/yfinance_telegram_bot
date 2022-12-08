from datetime import datetime
import yfinance as yf



def price_responses(input_text):
    user_message = str(input_text).upper()

    if user_message:
        ticker = yf.Ticker(str(user_message))
        price = ticker.info['regularMarketPrice']
        return(str(price))

    return "Please enter right symbol"
