# Calculating years to reach 25x annual expenses with a 66.6% savings rate
# Assuming real returns (returns adjusted for inflation) of 4% per annum
savings_rate = 2.0 / 3.0
expense_rate = 1.0 / 3.0

target_multiplier = 25  # 25x annual expenses
current_portfolio = 5.0 # You already have 60 months (5 years) of expenses saved!

portfolio = current_portfolio
years = 0
real_return_rate = 0.04  # Conservative real return above inflation

while portfolio < target_multiplier:
    portfolio = (portfolio * (1 + real_return_rate)) + (savings_rate / expense_rate)
    years += 1

print(f"Years required to hit FIRE: {years} years")
