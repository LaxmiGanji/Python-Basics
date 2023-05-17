
#using functions
def calculate_compound_interest(principal, rate, periods):
    rate = rate / 100
    amount = principal * (1 + rate) ** periods
    interest = amount - principal

    return interest
principal=int(input("enter the principle: "))
rate=int(input("enter the rate of interest: "))
periods=int(input("enter the time period: "))
compound_interest = calculate_compound_interest(principal, rate, periods)
print("Compound Interest:", compound_interest)

#without using functions
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
periods = int(input("Enter the number of periods: "))
rate = rate / 100
amount = principal * (1 + rate) ** periods
compound_interest = amount - principal
print("Compound Interest:", compound_interest)
