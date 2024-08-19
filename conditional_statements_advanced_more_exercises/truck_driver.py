season = input()
kms_a_month = float(input())

lv_per_km = 0

if kms_a_month <= 5000:
    if season == "Spring" or season == "Autumn":
        lv_per_km = 0.75
    elif season == "Summer":
        lv_per_km = 0.90
    else:
        lv_per_km = 1.05

elif 5000 < kms_a_month <= 10000:
    if season == "Spring" or season == "Autumn":
        lv_per_km = 0.95
    elif season == "Summer":
        lv_per_km = 1.10
    else:
        lv_per_km = 1.25

elif 10000 < kms_a_month <= 20000:
    lv_per_km = 1.45

gross_salary = 4 * kms_a_month * lv_per_km
net_salary = gross_salary - gross_salary * 0.10

print(f"{net_salary:.2f}")