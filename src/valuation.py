def calculate_book_value_per_share(balance_sheet):
    total_equity = balance_sheet.loc["Stockholders Equity"].values[0]
    total_shares_outstanding = balance_sheet.loc["Ordinary Shares Number"].values[0]
    if total_shares_outstanding == 0:
        return 0
    return total_equity / total_shares_outstanding

def calculate_pe_valuation(earnings_per_share, fair_pe_ratio):
    return earnings_per_share * fair_pe_ratio

def calculate_pb_valuation(book_value_per_share, fair_pb_ratio):
    return book_value_per_share * fair_pb_ratio

def calculate_graham_value(earnings_per_share, book_value_per_share):
    if earnings_per_share <= 0 or book_value_per_share <= 0:
        return 0
    return (22.5 * earnings_per_share * book_value_per_share) ** 0.5

def calculate_intrinsic_value(pe_valuation, pb_valuation, graham_value):
    """Average the valid (positive) estimates into one intrinsic value per share."""
    estimates = [v for v in (pe_valuation, pb_valuation, graham_value) if v > 0]
    if not estimates:
        return 0
    return sum(estimates) / len(estimates)

def calculate_target_buy_price(intrinsic_value, margin_of_safety=0.25):
    """Price you'd want to pay to have your chosen safety buffer, e.g. 25%."""
    return intrinsic_value * (1 - margin_of_safety)

def calculate_expected_upside(intrinsic_value, current_price):
    """How far the current price sits below (or above) intrinsic value."""
    if current_price == 0:
        return 0
    return (intrinsic_value - current_price) / current_price

def summarize_valuation(pe_valuation, pb_valuation, graham_value, intrinsic_value,
                         target_buy_price, current_price, expected_upside):
    return {
        "PE Valuation": pe_valuation,
        "PB Valuation": pb_valuation,
        "Graham Value": graham_value,
        "Intrinsic Value": intrinsic_value,
        "Target Buy Price (25% MoS)": target_buy_price,
        "Current Price": current_price,
        "Expected Upside": expected_upside,
        "Verdict": "Undervalued" if current_price <= target_buy_price
                   else ("Fair/Watch" if current_price <= intrinsic_value else "Overvalued")
    }