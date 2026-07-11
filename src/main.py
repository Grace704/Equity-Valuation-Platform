from data_loader import download_price_data, download_financial_statements
from statistics import (calculate_daily_returns, calculate_average_daily_return, 
calculate_annalized_return, calculate_annualized_volatility, calculate_sharpe_ratio)

ticker = input("Enter the stock ticker symbol: ").upper()
try:
    price, file_path = download_price_data(ticker)

    print(f"Saved price data to {file_path}")
    print(price.head())
    print(price.describe())

    daily_returns = calculate_daily_returns(price)
    print("Daily Returns:")
    print(daily_returns.head())

    average_daily_return = calculate_average_daily_return(daily_returns)
    print("Average Daily Return:")
    print(average_daily_return)

    annualized_return = calculate_annalized_return(daily_returns)
    print("Annualized Return:")
    print(annualized_return)

    annualized_volatility = calculate_annualized_volatility(daily_returns)
    print("Annualized Volatility:")
    print(annualized_volatility)

    sharpe_ratio = calculate_sharpe_ratio(daily_returns)
    print("Sharpe Ratio:")
    print(sharpe_ratio)

    income_statement, balance_sheet, cashflow = download_financial_statements(ticker)
    
    print("Income Statement:")
    print(income_statement.head())

    print("\nBalance Sheet:")
    print(balance_sheet.head())

    print("\nCash Flow Statement:")
    print(cashflow.head())

except ValueError as error:
    print(error)

