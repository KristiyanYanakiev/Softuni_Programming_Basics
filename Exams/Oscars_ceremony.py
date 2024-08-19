rent_hall = int(input())

statues = rent_hall - rent_hall * 0.30
cetering = statues - statues * 0.15
sound = cetering / 2

total = rent_hall + statues + cetering + sound

print(f"{total:.2f}")
