budget = float(input())
extras = int(input())
clothes_per_extra = float(input())

decor = budget * 0.10

if extras > 150:
    clothes_per_extra = clothes_per_extra - clothes_per_extra * 0.10

total = extras * clothes_per_extra + decor

if total > budget:
    print("Not enough money!")
    print(f"Wingard needs {total - budget:.2f} leva more")
elif total <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - total:.2f} leva left.")
