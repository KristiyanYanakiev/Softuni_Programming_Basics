letter_one = input()
last_letter = input()
skip_letter = input()

combination_counter = 0

for a in range(ord(letter_one), ord(last_letter) + 1):
    for b in range(ord(letter_one), ord(last_letter) + 1):
        for c in range(ord(letter_one), ord(last_letter) + 1):

            if chr(a) != skip_letter and chr(b) != skip_letter and chr(c) != skip_letter:
                combination_counter += 1

                print(f"{chr(a)}{chr(b)}{chr(c)}", end=" ")
print(combination_counter)





