n = input()

for x in range(1, int(n[2]) + 1):
    for y in range(1, int(n[1]) + 1):
        for z in range(1, int(n[0]) + 1):
            result = x * y * z

            print(f"{x} * {y} * {z} = {result};")




