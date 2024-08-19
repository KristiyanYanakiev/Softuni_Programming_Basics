from_limit = int(input())
to_limit = int(input())

for a in range(from_limit, to_limit + 1):
    for b in range(from_limit, to_limit + 1):
        for c in range(from_limit, to_limit + 1):
            for d in range(from_limit, to_limit + 1):
                if ((a % 2 == 0 and d % 2 != 0) or a % 2 != 0 and d % 2 == 0) and a > d and (b + c) % 2 == 0:
                    print(f"{a}{b}{c}{d}", end=" ")




