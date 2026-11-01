# Model the cash flow impact of moving from Bangalore to Bhubaneswar renting, then to Khurda owning
bangalore_exp = 100000 # Base assumption
bhubaneswar_renting_exp = bangalore_exp * 0.65 # ~35% drop in structural costs
khurda_owning_exp = bangalore_exp * 0.40 # ~60% drop from Bangalore (no rent, farm produce)

print(f"Bhubaneswar Phase Cost: ~{bhubaneswar_renting_exp:.0f}/month")
print(f"Khurda Phase Cost: ~{khurda_owning_exp:.0f}/month")
