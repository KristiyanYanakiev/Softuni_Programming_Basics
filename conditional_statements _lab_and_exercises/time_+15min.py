hours = int(input())
minutes = int(input()) + 15

if minutes > 59:
    minutes -= 60
    hours += 1

if hours > 23:
    hours -= 24

print(f"{hours}:{minutes:02d}")




