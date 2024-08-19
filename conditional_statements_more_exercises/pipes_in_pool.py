V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

liters_from_P1 = H * P1
liters_from_P2 = H * P2
total_liters = liters_from_P1 + liters_from_P2


fullness = (total_liters / V) * 100

per_cent_P1 = liters_from_P1 / total_liters * 100
per_cent_P2 = liters_from_P2 / total_liters * 100

if total_liters > V:
    print(f"For {H} hours the pool overflows with {total_liters - V} liters.")
else:
    print(f"The pool is {fullness}% full. Pipe 1: {per_cent_P1:.2f}%. Pipe 2: {per_cent_P2:.2f}%.")