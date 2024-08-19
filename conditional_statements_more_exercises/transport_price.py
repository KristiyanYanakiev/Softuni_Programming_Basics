n_kms = int(input())
day_or_night = input()

price_taxi = 0
price_bus = 0
price_train = 0

if day_or_night == "day":
    price_taxi = n_kms * 0.79 + 0.70
    price_bus = n_kms * 0.09
    price_train = n_kms * 0.06
elif day_or_night == "night":
    price_taxi = n_kms * 0.90 + 0.70
    price_bus = n_kms * 0.09
    price_train = n_kms * 0.06

if n_kms < 20:
    print(f"{price_taxi:.2f}")
elif 20 <= n_kms < 100:
    print(f"{price_bus:.2f}")
elif n_kms >= 100:
    print(f"{price_train:.2f}")




