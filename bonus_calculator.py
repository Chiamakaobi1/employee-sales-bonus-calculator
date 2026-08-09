def calculate_bonus(sales):
    if sales >= 1000000:
        bonus_rate = 0.10
    elif sales >= 500000:
        bonus_rate = 0.07
    elif sales >= 250000:
        bonus_rate = 0.05
    else:
        bonus_rate = 0.02

    bonus = sales * bonus_rate
    return bonus


sales = float(input("Enter employee sales amount: ₦"))

bonus = calculate_bonus(sales)

print(f"Employee sales: ₦{sales:,.2f}")
print(f"Bonus earned: ₦{bonus:,.2f}")
