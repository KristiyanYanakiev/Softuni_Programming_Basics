floors = int(input())
flats_per_floor = int(input())

apartment_name = ""


for i in range(floors, 0, -1):
    for j in range(flats_per_floor):

        if i == floors:
            apartment_name = f"L{i}{j}"
        elif i % 2 == 0:
            apartment_name = f"O{i}{j}"
        elif i % 2 != 0:
            apartment_name = f"A{i}{j}"

        print(apartment_name, end=" ")
    print()

