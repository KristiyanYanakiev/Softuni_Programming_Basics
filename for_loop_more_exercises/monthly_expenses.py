period_of_time_in_months = int(input())

water_per_month = 20
internet_per_month = 15

total_electricity = 0
total_water = 0
total_internet = 0
total_other = 0

total = 0

for _ in range(period_of_time_in_months):
    electricity_per_month = float(input())
    total_electricity += electricity_per_month
    total_water += 20
    total_internet += 15
    total_other += (electricity_per_month + water_per_month + internet_per_month) + \
                   (electricity_per_month + water_per_month + internet_per_month) * 0.20

total = total_water + total_internet + total_other + total_electricity

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {total / period_of_time_in_months:.2f} lv")
