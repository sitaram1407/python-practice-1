# Quick cash runway validation for a mid-career IT professional transitioning to business
monthly_expenses = 1.0  # Normalized base unit
years_of_runway = 5
total_corpus = monthly_expenses * 12 * years_of_runway

# Standard assumption: Business takes 24 months to break even, and requires initial capital
business_setup_cost = monthly_expenses * 12  # 1 year of expenses for initial capex/opex
remaining_survival_runway = total_corpus - business_setup_cost
remaining_years = remaining_survival_runway / (monthly_expenses * 12)

print(f"Total Corpus: {total_corpus} months of expenses")
print(f"Remaining Survival Runway after business setup: {remaining_years:.1f} years")
