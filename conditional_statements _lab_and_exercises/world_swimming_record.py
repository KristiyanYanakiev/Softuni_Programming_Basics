record = float(input())
distance = float(input())
seconds_per_one_meter = float(input())

resistance = distance // 15 * 12.5


result = distance * seconds_per_one_meter + resistance

if result < record:
    print(f"Yes, he succeeded! The new world record is {result:.2f} seconds.")
elif result >= record:
    print(f"No, he failed! He was {result - record:.2f} seconds slower.")

