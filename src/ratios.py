def calculate_net_profit_margin(income_statement):
   revenue = income_statement.loc["Total Revenue"].values[0]
   net_income = income_statement.loc["Net Income"].values[0]
   if revenue == 0:
        return 0
   net_profit_margin = net_income / revenue
   return net_profit_margin

def calculate_current_ratio(balance_sheet):
    current_assets = balance_sheet.loc["Current Assets"].values[0]
    current_liabilities = balance_sheet.loc["Current Liabilities"].values[0]
    if current_liabilities == 0:
          return 0
    current_ratio = current_assets / current_liabilities
    return current_ratio

def calculate_debt_to_equity_ratio(balance_sheet):
    total_liabilities = balance_sheet.loc["Total Liabilities Net Minority Interest"].values[0]
    total_equity = balance_sheet.loc["Total Stockholder Equity"].values[0]
    if total_equity == 0:
        return 0
    debt_to_equity_ratio = total_liabilities / total_equity
    return debt_to_equity_ratio

def calculate_debt_to_assets_ratio(balance_sheet):
    total_liabilities = balance_sheet.loc["Total Liabilities Net Minority Interest"].values[0]
    total_assets = balance_sheet.loc["Total Assets"].values[0]
    if total_assets == 0:
        return 0
    debt_to_assets_ratio = total_liabilities / total_assets
    return debt_to_assets_ratio

def calculate_return_on_equity(income_statement, balance_sheet):
    net_income = income_statement.loc["Net Income"].values[0]
    total_equity = balance_sheet.loc["Total Stockholder Equity"].values[0]
    if total_equity == 0:
        return 0
    return_on_equity = net_income / total_equity
    return return_on_equity

def calculate_return_on_assets(income_statement, balance_sheet):
    net_income = income_statement.loc["Net Income"].values[0]
    total_assets = balance_sheet.loc["Total Assets"].values[0]
    if total_assets == 0:
        return 0
    return_on_assets = net_income / total_assets
    return return_on_assets

def calculate_operating_margin(income_statement):
    operating_income = income_statement.loc["Operating Income or Loss"].values[0]
    revenue = income_statement.loc["Total Revenue"].values[0]
    if revenue == 0:
        return 0
    operating_margin = operating_income / revenue
    return operating_margin

def calculate_asset_turnover_ratio(income_statement, balance_sheet):
    revenue = income_statement.loc["Total Revenue"].values[0]
    total_assets = balance_sheet.loc["Total Assets"].values[0]
    if total_assets == 0:
        return 0
    asset_turnover_ratio = revenue / total_assets
    return asset_turnover_ratio

def calculate_earnings_per_share(income_statement, balance_sheet):
    net_income = income_statement.loc["Net Income"].values[0]
    total_shares_outstanding = balance_sheet.loc["Common Stock"].values[0]
    if total_shares_outstanding == 0:
        return 0
    earnings_per_share = net_income / total_shares_outstanding
    return earnings_per_share

def calculate_price_to_earnings_ratio(price_data, income_statement, balance_sheet):
    earnings_per_share = calculate_earnings_per_share(income_statement, balance_sheet)
    if earnings_per_share == 0:
        return 0
    latest_price = price_data["Close"].iloc[-1]
    price_to_earnings_ratio = latest_price / earnings_per_share
    return price_to_earnings_ratio

def calculate_price_to_book_ratio(price_data, balance_sheet):
    total_equity = balance_sheet.loc["Total Stockholder Equity"].values[0]
    total_shares_outstanding = balance_sheet.loc["Common Stock"].values[0]
    if total_shares_outstanding == 0:
        return 0
    book_value_per_share = total_equity / total_shares_outstanding
    latest_price = price_data["Close"].iloc[-1]
    if book_value_per_share == 0:
        return 0
    price_to_book_ratio = latest_price / book_value_per_share
    return price_to_book_ratio

def calculate_price_to_sales_ratio(price_data, income_statement, balance_sheet):
    revenue = income_statement.loc["Total Revenue"].values[0]
    total_shares_outstanding = balance_sheet.loc["Common Stock"].values[0]
    if total_shares_outstanding == 0:
        return 0
    sales_per_share = revenue / total_shares_outstanding
    latest_price = price_data["Close"].iloc[-1]
    if sales_per_share == 0:
        return 0
    price_to_sales_ratio = latest_price / sales_per_share
    return price_to_sales_ratio

def calculate_revenue_growth(income_statement):
    recent_revenue = income_statement.loc["Total Revenue"].values[0]
    previous_revenue = income_statement.loc["Total Revenue"].values[1]
    if previous_revenue == 0:
        return 0
    revenue_growth = (recent_revenue - previous_revenue) / previous_revenue
    return revenue_growth