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
    calculate_revenue_growth,
    calculate_net_income_growth,
    calculate_free_cash_flow_growth)

from valuation import (
    calculate_book_value_per_share,
    calculate_pe_valuation,
    calculate_pb_valuation,
    calculate_graham_value,
    calculate_intrinsic_value,
    calculate_target_buy_price,
    calculate_expected_upside,
    summarize_valuation)

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

    earnings_per_share = calculate_earnings_per_share(income_statement, balance_sheet)
    print("Earnings Per Share:")
    print(earnings_per_share)

    price_to_earnings = calculate_price_to_earnings_ratio(price, income_statement, balance_sheet)
    print("Price-to-Earnings Ratio:")
    print(price_to_earnings)
    
    price_to_book = calculate_price_to_book_ratio(price, balance_sheet)
    print("Price-to-Book Ratio:")
    print(price_to_book)

    return_on_equity = calculate_return_on_equity(income_statement, balance_sheet)
    print("Return on Equity:")
    print(return_on_equity)

    debt_to_equity = calculate_debt_to_equity_ratio(balance_sheet)
    print("Debt-to-Equity Ratio:")
    print(debt_to_equity)

    operating_margin = calculate_operating_margin(income_statement)
    print("Operating Margin:")
    print(operating_margin)
    
    asset_turnover = calculate_asset_turnover_ratio(income_statement, balance_sheet)
    print("Asset Turnover Ratio:")
    print(asset_turnover)
    
    revenue_growth = calculate_revenue_growth(income_statement)
    print("Revenue Growth:")
    print(revenue_growth)

    net_income_growth = calculate_net_income_growth(income_statement)
    print("Net Income Growth:")
    print(net_income_growth)

    free_cash_flow_growth = calculate_free_cash_flow_growth(cashflow)
    print("Free Cash Flow Growth:")
    print(free_cash_flow_growth)

    book_value_per_share = calculate_book_value_per_share(balance_sheet)
    current_price = price["Close"].dropna().iloc[-1]

    fair_pe_ratio = float(input("Enter a fair P/E ratio for this stock (e.g. 15): "))
    fair_pb_ratio = float(input("Enter a fair P/B ratio for this stock (e.g. 1.5): "))

    pe_valuation = calculate_pe_valuation(earnings_per_share, fair_pe_ratio)
    pb_valuation = calculate_pb_valuation(book_value_per_share, fair_pb_ratio)
    graham_value = calculate_graham_value(earnings_per_share, book_value_per_share)

    intrinsic_value = calculate_intrinsic_value(pe_valuation, pb_valuation, graham_value)
    target_buy_price = calculate_target_buy_price(intrinsic_value, margin_of_safety=0.25)
    expected_upside = calculate_expected_upside(intrinsic_value, current_price)

    valuation_summary = summarize_valuation(
        pe_valuation, pb_valuation, graham_value,
        intrinsic_value, target_buy_price, current_price, expected_upside)

    print("\nValuation Summary:")
    for key, value in valuation_summary.items():
        print(f"{key}: {value}")

except ValueError as error:
    print(error)

