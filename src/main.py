from data_loader import download_price_data, download_financial_statements
from statistics import (
    calculate_daily_returns, 
    calculate_average_daily_return, 
    calculate_annalized_return, 
    calculate_annualized_volatility, 
    calculate_sharpe_ratio)
from ratios import (
    calculate_net_profit_margin,
    calculate_current_ratio,
    calculate_debt_to_assets_ratio,
    calculate_return_on_assets,
    calculate_earnings_per_share,
    calculate_price_to_earnings_ratio,
    calculate_price_to_book_ratio,
    calculate_return_on_equity,
    calculate_debt_to_equity_ratio,
    calculate_operating_margin,
    calculate_asset_turnover_ratio,
    calculate_revenue_growth)
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
    
    net_profit_margin = calculate_net_profit_margin(income_statement)
    print("Net Profit Margin:")
    print(net_profit_margin)

    current_ratio = calculate_current_ratio(balance_sheet)
    print("Current Ratio:")
    print(current_ratio)

    debt_to_assets = calculate_debt_to_assets_ratio(balance_sheet)
    print("Debt-to-Assets Ratio:")
    print(debt_to_assets)

    return_on_assets = calculate_return_on_assets(income_statement, balance_sheet)
    print("Return on Assets:")
    print(return_on_assets)

except ValueError as error:
    print(error)

