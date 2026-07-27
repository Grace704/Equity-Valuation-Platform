def calculate_daily_returns(price_data):
    daily_returns = price_data["Close"].pct_change()
    return daily_returns

def calculate_average_daily_return(daily_returns):
    average_daily_return = daily_returns.mean()
    return average_daily_return

def calculate_annalized_return(daily_returns, trading_days=252):
    average_daily_return = calculate_average_daily_return(daily_returns)
    annualized_return = (1 + average_daily_return) ** trading_days - 1 
    """Future Value = Present Value × (1 + return)^number_of_periods"""
    return annualized_return

def calculate_annualized_volatility(daily_returns, trading_days=252):
    daily_volatility = daily_returns.std()
    annualized_volatility = daily_volatility * (trading_days ** 0.5)
    return annualized_volatility

def calculate_sharpe_ratio(daily_returns, risk_free_rate=0.01, trading_days=252):
    annualized_return = calculate_annalized_return(daily_returns, trading_days)
    annualized_volatility = calculate_annualized_volatility(daily_returns, trading_days)
    sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility
    return sharpe_ratio

def calculate_max_drawdown(price_data):
    daily_returns = price_data["Close"].pct_change(fill_method=None).dropna()
    cumulative_returns = (1 + price_data["Close"].pct_change(fill_method=None)).cumprod()
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    max_drawdown = drawdown.min()
    return max_drawdown
