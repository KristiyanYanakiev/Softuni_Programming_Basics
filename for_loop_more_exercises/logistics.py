number_of_weights = int(input())
total_of_tones = 0
microbus_tones = 0
truck_tones = 0
train_tones = 0

total_price = 0


for _ in range(number_of_weights):
    tones_of_each_weight = int(input())
    total_of_tones += tones_of_each_weight
    if tones_of_each_weight <= 3:
        total_price += 200 * tones_of_each_weight
        microbus_tones += tones_of_each_weight
    elif 4 <= tones_of_each_weight <= 11:
        total_price += 175 * tones_of_each_weight
        truck_tones += tones_of_each_weight
    elif tones_of_each_weight >= 12:
        total_price += 120 * tones_of_each_weight
        train_tones += tones_of_each_weight

average_per_tone = total_price / total_of_tones

print(f"{average_per_tone:.2f}")
print(f"{microbus_tones / total_of_tones * 100:.2f}%")
print(f"{truck_tones / total_of_tones * 100:.2f}%")
print(f"{train_tones / total_of_tones * 100:.2f}%")

