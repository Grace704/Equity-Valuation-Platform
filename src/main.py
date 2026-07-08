from data_loader import download_price_data
ticker = input("Enter the stock ticker symbol: ").upper()
price = download_price_data(ticker)
print(price.head())
print(price.describe())