n = int(input())

liters_counter = 0
degrees_counter = 0

for _ in range(n):
    quantity = float(input())
    degrees = float(input())
    liters_counter += quantity

    degrees_for_the_day = quantity * degrees
    degrees_counter += degrees_for_the_day

average_degrees = degrees_counter / liters_counter

print(f"Liter: {liters_counter:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print(f"Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print(f"Super!")
else:
    print("Dilution with distilled water!")
