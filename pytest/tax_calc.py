def calculate_tax(earnings):
    if earnings < 12000:
       
        tax = 0
    elif earnings <= 36000:
       
        taxable_earnings = earnings - 12000
        tax = 0.20 * taxable_earnings
    else:
        
        taxable_earnings = earnings - 36000
        tax = 0.40 * taxable_earnings

    return tax


earnings = float(input("Enter your annual earnings: "))
tax = calculate_tax(earnings)

print(f"Tax to be paid: ${tax:.2f}")
