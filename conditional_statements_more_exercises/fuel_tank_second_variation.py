type_fuel = input()
liters_fuel = float(input())

if liters_fuel >= 25:
    if type_fuel == "Diesel":
        print("You have enough diesel.")
    elif type_fuel == "Gasoline":
        print("You have enough gasoline.")
    elif type_fuel == "Gas":
        print("You have enough gas.")
    else:
        print("Invalid fuel!")
elif liters_fuel < 25:
    if type_fuel == "Diesel":
        print("Fill your tank with diesel!")
    elif type_fuel == "Gasoline":
        print("Fill your tank with gasoline!")
    elif type_fuel == "Gas":
        print("Fill your tank with gas!")
    else:
        print("Invalid fuel!")
