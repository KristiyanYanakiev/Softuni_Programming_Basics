length, width, height = int(input()), int(input()), int(input())
volume_filled = float(input()) / 100

volume = (length * width * height) / 1000

remaining_volume = volume - volume * volume_filled

print(remaining_volume)


