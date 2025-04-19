from datetime import datetime, timedelta

def calculate_fd_interest(principal, rate, start_date_str, duration_days):
    # End of current financial year (FY ends on March 31st)
    FY_END = datetime(datetime.now().year if datetime.now().month <= 3 else datetime.now().year + 1, 3, 31)

    # Convert start date string to datetime object
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

    # Calculate maturity date by adding days
    maturity_date = start_date + timedelta(days=duration_days)

    # Use the earlier date between maturity and FY end
    end_date = min(maturity_date, FY_END)

    # Calculate active days in this FY
    days_active = (end_date - start_date).days
    if days_active <= 0:
        return 0

    # Annual interest and prorated for days active
    annual_interest = principal * rate / 100
    interest_earned = annual_interest * (days_active / 365)

    return round(interest_earned, 2)

# Input section
principal = int(input("Enter the amount you are depositing: "))
rate = float(input("What is the interest rate (don’t put % symbol): "))
start_date = input("Enter the date in this format: \"2025-01-15\" : ")
duration_days = int(input("The duration in days: "))

# Call function
interest = calculate_fd_interest(principal, rate, start_date, duration_days)
print(f"Interest earned in this FY: ₹{interest}")
