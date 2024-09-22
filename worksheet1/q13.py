def compound_interest(principal, rate, time):
    # Calculate the final amount
    amount = principal * (1 + rate / 100) ** time
    # Compound interest is amount minus the principal
    ci = amount - principal
    return ci


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

ci = compound_interest(principal, rate, time)
print(f"The compound interest is: {ci:.2f}")