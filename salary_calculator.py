# Egypt Remote Salary Calculator 🇪🇬💰
# Project #2 by Zainab from Sialkot to Cairo

print("=== Egypt Remote Salary Calculator ===")

# User se salary lo
usd_salary = float(input("Monthly salary in USD: $"))

# USD to PKR rate lo  
usd_rate = float(input("1 USD = Kitne PKR? "))

# Calculation
monthly_pkr = usd_salary * usd_rate
yearly_pkr = monthly_pkr * 12
tax = yearly_pkr * 0.05  # 5% tax
net_yearly = yearly_pkr - tax

print("\n--- Tumhari Salary Report ---")
print(f"Monthly: {monthly_pkr:,.0f} PKR")
print(f"Yearly: {yearly_pkr:,.0f} PKR")
print(f"5% Tax: {tax:,.0f} PKR") 
print(f"Net Yearly: {net_yearly:,.0f} PKR")

if usd_salary >= 400:
    print("\nMubarak ho! $400+ target complete 🎯")
else:
    print(f"\n${400 - usd_salary} aur chahiye $400 target ke liye")

print("\nSialkot se Cairo tak, hisaab clear 💰")
