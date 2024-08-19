bitcoin_amount = int(input())
yoans_amount = float(input())
commission = float(input()) / 100

total_lv = bitcoin_amount * 1168 + yoans_amount * 0.15 * 1.76

total_eur = total_lv / 1.95

final = total_eur - total_eur * commission

print(f"{final:.2f}")