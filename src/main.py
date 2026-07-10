from data_loader import download_price_data, download_financial_statements
ticker = input("Enter the stock ticker symbol: ").upper()
try:
    price, file_path = download_price_data(ticker)
    print(price.head())
    print(price.describe())
    income_statement, balance_sheet, cashflow = download_financial_statements(ticker)
    print("Income Statement:")
    print(income_statement.head())
    print("\nBalance Sheet:")
    print(balance_sheet.head())
    print("\nCash Flow Statement:")
    print(cashflow.head())
    print(f"Saved price data to {file_path}")
except ValueError as error:
    print(error)