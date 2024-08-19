type_fuel = input()
liters_fuel = float(input())

if liters_fuel >= 25 and (type_fuel == "Diesel" or type_fuel == "Gasoline" or type_fuel == "Gas"):
    print(f"You have enough {type_fuel}.")
elif liters_fuel < 25 and (type_fuel == "Diesel" or type_fuel == "Gasoline" or type_fuel == "Gas"):
    print(f"Fill your tank with {type_fuel}!")
else:
    print("Invalid fuel!")