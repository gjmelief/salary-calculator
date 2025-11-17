# Dutch Salary Calculator
# Version 0.2 - First version - 17-11-2025
def main():
    # Display the title
    print("\n=== Dutch Salary Calculator ===")

    # Setting the tax_rates
    tax_rate_low = 0.3697
    tax_rate_high = 0.4950
    tax_bracket_limit = 38098  # Amount that is taxed with the low rate

    # Ask the user for their gross yearly salary and vacation money %
    salary = float(input("\nPlease enter your gross salary for 2025 (€): "))
    vacation_perc = float(input("Is your vacation money percentage 8% or 8,33%? "))

    # Set helper tax calculations
    # Amount that is taxed with the high rate
    taxed_high = salary - tax_bracket_limit
    # Maximum amount when tax bracket is reached
    tax_bracket_limit_amount = tax_bracket_limit * tax_rate_low

    # Calculate the net salary
    # First determine if tax bracket limit is reached
    if salary <= tax_bracket_limit:
        high_rate = False
    else:
        high_rate = True

    # Calculate the net salary when tax bracket is not reached
    low_tax_amount = salary * tax_rate_low
    if not high_rate:
        total_tax = low_tax_amount
        net_salary = salary - total_tax
    # Calculate the net salary when tax bracket is reached
    else:
        high_tax_amount = taxed_high * tax_rate_high
        total_tax = tax_bracket_limit_amount + high_tax_amount
        net_salary = salary - total_tax

    # Calculate vacation money
    vacation_money = (vacation_perc / 100) * salary

    # Calculate total net per year
    total_net_per_year = net_salary + vacation_money

    # Calculate net per month
    net_per_month = net_salary / 12

    # Output the results in a neat manner
    print("\n=== Results ===")
    print(f"Gross salary: \t\t€{salary:.2f}")
    print(f"Tax paid: \t\t€{total_tax:.2f}")
    print(f"Net salary: \t\t€{net_salary:.2f}")
    print(f"Vacation money: \t€{vacation_money:.2f}")
    print(f"Total Net per year: \t€{total_net_per_year:.2f}")
    print(f"Net per month: \t\t€{net_per_month:.2f}")


if __name__ == "__main__":
    main()