budget = float(input())
nights_count = int(input())
price_per_night = float(input())
per_cent_additional_expenses = int(input()) / 100

if nights_count > 7:
    price_per_night = price_per_night - price_per_night * 0.05

total = price_per_night * nights_count
added = budget * per_cent_additional_expenses

final = total + added

if budget >= final:
    print(f"Ivanovi will be left with {budget - final:.2f} leva after vacation.")
else:
    print(f"{final - budget:.2f} leva needed.")


