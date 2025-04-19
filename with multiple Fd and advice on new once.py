from datetime import datetime, timedelta

def calculate_fd_interest(principal, rate, start_date_str, duration_days):
    FY_END = datetime(datetime.now().year if datetime.now().month <= 3 else datetime.now().year + 1, 3, 31)
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y")  # Updated date format: dd-mm-yyyy
    maturity_date = start_date + timedelta(days=duration_days)
    end_date = min(maturity_date, FY_END)
    days_active = (end_date - start_date).days
    if days_active <= 0:
        return 0
    annual_interest = principal * rate / 100
    interest_earned = annual_interest * (days_active / 365)
    return round(interest_earned, 2)

print("FD INTEREST CALCULATOR FOR CURRENT FY")
print("--------------------------------------")

fd_list = []
total_interest = 0

num_fds = int(input("How many FDs do you have? "))

for i in range(num_fds):
    print(f"\nEnter details for FD {i+1} (Date format: dd-mm-yyyy):")
    principal = int(input("→ Amount you are depositing (₹): "))
    rate = float(input("→ Interest rate (without %): "))
    start_date = input("→ Start date (dd-mm-yyyy): ")
    duration_days = int(input("→ Duration (in days): "))
    interest = calculate_fd_interest(principal, rate, start_date, duration_days)
    total_interest += interest
    fd_list.append({
        "amount": principal,
        "rate": rate,
        "start_date": start_date,
        "duration_days": duration_days,
        "interest": interest
    })
    print(f"✅ Interest for FD {i+1} in current FY: ₹{interest:,.2f}")

print("\n-----------------------------")
print("📊 SUMMARY FOR ALL FDs IN FY:")
print("-----------------------------")
for i, fd in enumerate(fd_list, 1):
    print(f"FD {i}: ₹{fd['amount']:,.0f} @ {fd['rate']}% from {fd['start_date']} ➝ ₹{fd['interest']:,.2f} earned")

print(f"\n🔢 Total FD interest this FY: ₹{total_interest:,.2f}")

from datetime import datetime, timedelta

# Determine TDS limit based on financial year
current_year = datetime.now().year if datetime.now().month <= 3 else datetime.now().year + 1
TDS_LIMIT = 40000 if current_year < 2025 else 50000

# Ask for new FD details
print("\n🎯 NEW FD PLANNER")
new_fd_principal = int(input("→ Amount you want to invest now (₹): "))
new_fd_rate = float(input("→ Interest rate (without %): "))
new_fd_duration = int(input("→ Duration (in days): "))

# Try different start dates from today until March 31st to avoid crossing TDS
today = datetime.now()
FY_END = datetime(current_year, 3, 31)
best_start_date = None

for offset in range(0, (FY_END - today).days):
    try_date = today + timedelta(days=offset)
    interest = calculate_fd_interest(new_fd_principal, new_fd_rate, try_date.strftime("%d-%m-%Y"), new_fd_duration)
    if (total_interest + interest) <= TDS_LIMIT:
        best_start_date = try_date.strftime("%d-%m-%Y")
        break

# Output suggestion
print("\n-----------------------------")
if best_start_date:
    print(f"🗓️ To stay under TDS limit of ₹{TDS_LIMIT:,}, start your new FD on: {best_start_date}")
    print(f"Projected interest for this FY from new FD: ₹{interest:,.2f}")
    print(f"New total interest (with all FDs): ₹{(total_interest + interest):,.2f}")
else:
    print("⚠️ No safe date found! Any new FD this FY will likely exceed the TDS limit.")

TDS_LIMIT = 40000
if total_interest > TDS_LIMIT:
    print("⚠️ ALERT: Your total interest crosses ₹40,000. TDS might be deducted by your bank.")
else:
    print("✅ You're under the ₹40,000 TDS limit for this FY.")
