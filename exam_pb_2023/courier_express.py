package_weight = float(input())
service_type = input()
distance = int(input())

price_per_km = 0
extra_cost_per_km = 0

if package_weight < 1:
    if service_type == "standard":
        price_per_km = 3
    else:
        price_per_km = 3
        extra_cost_per_km = package_weight * (0.8 * 3)


elif 1 <= package_weight < 10:
    if service_type == "standard":
        price_per_km = 5
    else:
        price_per_km = 5
        extra_cost_per_km = package_weight * (0.4 * 5)

elif 10 <= package_weight < 40:
    if service_type == "standard":
        price_per_km = 10
    else:
        price_per_km = 10
        extra_cost_per_km = package_weight * (0.05 * 10)

elif 40 <= package_weight < 90:
    if service_type == "standard":
        price_per_km = 15
    else:
        price_per_km = 15
        extra_cost_per_km = package_weight * (0.02 * 15)

elif 90 <= package_weight < 150:
    if service_type == "standard":
        price_per_km = 20
    else:
        price_per_km = 20
        extra_cost_per_km = package_weight * (0.01 * 20)

total_price = (price_per_km * distance + extra_cost_per_km * distance) / 100


print(f"The delivery of your shipment with weight of {package_weight:.3f} kg. would cost {total_price:.2f} lv.")
