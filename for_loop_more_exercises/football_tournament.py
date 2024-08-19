stadium_capacity = int(input())
number_of_fans = int(input())

A = 0
B = 0
V = 0
G = 0

fans_team_1 = 0
fans_team_2 = 0

for _ in range(number_of_fans):
    sector = input()
    if sector == "A":
        A += 1
        fans_team_1 += 1
    elif sector == "B":
        B += 1
        fans_team_1 += 1
    elif sector == "V":
        V += 1
        fans_team_2 += 1
    elif sector == "G":
        G += 1
        fans_team_2 += 1

print(f"{A / number_of_fans * 100:.2f}%")
print(f"{B / number_of_fans * 100:.2f}%")
print(f"{V / number_of_fans * 100:.2f}%")
print(f"{G / number_of_fans * 100:.2f}%")
print (f"{number_of_fans / stadium_capacity * 100:.2f}%")
