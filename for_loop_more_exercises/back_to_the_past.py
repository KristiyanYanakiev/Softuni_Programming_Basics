inhereted_money = float(input())
until_year = int(input())

age = 18

for i in range(1800, until_year + 1):
    if i == 1800:
        age = 18
    else:
        age += 1
    if i % 2 == 0:
        inhereted_money -= 12_000
    else:
        inhereted_money -= 12_000 + 50 * age

if inhereted_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inhereted_money:.2f} dollars left.")
else:
    print(f"He will need {abs(inhereted_money):.2f} dollars to survive.")