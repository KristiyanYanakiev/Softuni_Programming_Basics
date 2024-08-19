money_per_day_from_parents = float(input())
money_won_per_day = float(input())
expenses_for_whole_period = float(input())

price_of_present = float(input())

total_profit = money_per_day_from_parents * 5 + money_won_per_day * 5 - expenses_for_whole_period

if total_profit >= price_of_present:
    print(f"Profit: {total_profit:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {price_of_present - total_profit:.2f} BGN.")

