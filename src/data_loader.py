import os
import pandas as pd
import yfinance as yf

def download_price_data(ticker): 
    """Downloads historical stock price data for a given ticker symbol and saves it as a CSV file."""
    stock = yf.Ticker(ticker)
    price = stock.history(period="5y")
    if price.empty:
        raise ValueError(f"No data found for ticker symbol: {ticker}")
    os.makedirs("data/raw", exist_ok=True)
    file_path = f"data/raw/{ticker}_price.csv"
    price.to_csv(file_path, index_label="Date")
    return price, file_path

def load_price_data(ticker):
    """Loads historical stock price data for a given ticker symbol from a CSV file."""
    file_path = f"data/raw/{ticker}_price.csv"
    price = pd.read_csv(file_path, index_col="Date", parse_dates=True)
    return price

def download_financial_statements(ticker):
    """Downloads financial statements for a given ticker symbol and saves them as CSV files."""
    stock = yf.Ticker(ticker)
    income_statement = stock.financials
    balance_sheet = stock.balance_sheet
    cashflow = stock.cashflow
    if income_statement.empty or balance_sheet.empty or cashflow.empty:
        raise ValueError(f"No financial statements found for ticker symbol: {ticker}")
    os.makedirs("data/raw", exist_ok=True)
    income_statement.to_csv(f"data/raw/{ticker}_income_statement.csv")
    balance_sheet.to_csv(f"data/raw/{ticker}_balance_sheet.csv")
    cashflow.to_csv(f"data/raw/{ticker}_cashflow.csv")
    return income_statement, balance_sheet, cashflow

