import sys

max_number = - sys.maxsize

while True:
    number = input()
    if number != "Stop":
        if int(number) > max_number:
            max_number = int(number)
    else:
        print(max_number)
        break