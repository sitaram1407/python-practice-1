def calculate_fire_accumulation():
    # 1. Base Assumptions (Normalized to current Bangalore monthly expenses = 1.0 Unit)
    monthly_expense = 1.0
    annual_expense = monthly_expense * 12
    
    # You invest 2/3rd of net salary and live on 1/3rd. 
    # This means your annual savings = 2 times your annual expenses.
    total_annual_savings = annual_expense * 2 
    
    # 2. Ring-fenced Kids Contributions (Deducted from the savings pool)
    ssy_annual = 1.50 / 12  # ₹1.5L max in units (Assuming 1 Unit = ₹1L/month expense as baseline)
    ppf_annual = 1.50 / 12
    kids_deduction = ssy_annual + ppf_annual
    
    # Net annual surplus moving into your main FIRE portfolio (Arbitrage/MFs)
    net_annual_investment = total_annual_savings - kids_deduction
    
    # 3. Starting Assets
    current_portfolio = monthly_expense * 60 # 60 months of expenses currently held
    
    # 4. Growth Rates (Conservative real returns adjusted for inflation)
    portfolio_real_return = 0.04 # 4% above inflation for a blended MF/Arbitrage basket
    
    # 5. The 6.5 Year Projection Loop
    years = 6.5
    portfolio = current_portfolio
    
    # Calculate full years first
    for year in range(int(years)):
        portfolio = (portfolio * (1 + portfolio_real_return)) + net_annual_investment
        
    # Add the remaining 0.5 fractional year
    portfolio = (portfolio * (1 + (portfolio_real_return * 0.5))) + (net_annual_investment * 0.5)
    
    # 6. Print Results out in clear expense multiples
    print("=" * 55)
    print(f"STATUS AT THE END OF YOUR 6.5-YEAR CORPORATE SPRINT:")
    print("=" * 55)
    print(f"Initial Portfolio Cushion : {current_runway(current_portfolio)}")
    print(f"Projected Total Corpus    : {current_runway(portfolio)}")
    print(f"Target FIRE Number        : 25.0x Annual Expenses")
    print("-" * 55)
    
    # Factor in the structural cost deflation when moving to Bhubaneswar
    bhubaneswar_multiplier = 1.45 # Cost drops by ~30%, expanding the runway value by ~45%
    adjusted_runway = portfolio * bhubaneswar_multiplier
    print(f"Adjusted Runway Value in Bhubaneswar: {current_runway(adjusted_runway)}")
    print("=" * 55)

def current_runway(value):
    years = value / 12
    return f"{value:.1f} months of expenses ({years:.1f} years of life)"

if __name__ == "__main__":
    calculate_fire_accumulation()
