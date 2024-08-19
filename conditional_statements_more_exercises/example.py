type_fuel = input()
liters_fuel = float(input())

correct_data = True

if type_fuel == "Diesel" or type_fuel == "Gasoline" or type_fuel == "Gas":
    correct_data = True
else:
    correct_data = False

if correct_data:
    if liters_fuel >= 25:
        print(f"You have enough {type_fuel}.")
    elif liters_fuel < 25:
        print(f"Fill your tank with {type_fuel}!")
else:
    print("Invalid fuel!")