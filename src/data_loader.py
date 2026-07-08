import os
import yfinance as yf

def download_price_data(ticker): 
    """Downloads historical stock price data for a given ticker symbol and saves it as a CSV file."""
    stock = yf.Ticker(ticker)
    price = stock.history(period="5y")
    os.makedirs("data/raw", exist_ok=True)
    file_path = f"data/raw/{ticker}_price.csv"
    price.to_csv(file_path)
    return price