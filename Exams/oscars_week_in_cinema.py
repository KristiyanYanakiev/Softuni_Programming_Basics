movie = input()
type_hall = input()
number_of_sold_tickets = int(input())

ticket_price = 0

if movie == "A Star Is Born":
    if type_hall == "normal":
        ticket_price = 7.50
    elif type_hall == "luxury":
        ticket_price = 10.50
    else:
        ticket_price = 13.50

elif movie == "Bohemian Rhapsody":
    if type_hall == "normal":
        ticket_price = 7.35
    elif type_hall == "luxury":
        ticket_price = 9.45
    else:
        ticket_price = 12.75

elif movie == "Green Book":
    if type_hall == "normal":
        ticket_price = 8.15
    elif type_hall == "luxury":
        ticket_price = 10.25
    else:
        ticket_price = 13.25

else:
    if type_hall == "normal":
        ticket_price = 8.75
    elif type_hall == "luxury":
        ticket_price = 11.55
    else:
        ticket_price = 13.95

total = number_of_sold_tickets * ticket_price

print(f"{movie} -> {total:.2f} lv.")
