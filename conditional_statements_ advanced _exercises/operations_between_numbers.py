N1 = int(input())
N2 = int(input())
operator = input()
result = 0
final = ""


if operator == "+":
    result = N1 + N2
    if result % 2 == 0:
        final = f"{N1} {operator} {N2} = {result} - even"
    else:
        final = f"{N1} {operator} {N2} = {result} - odd"
elif operator == "-":
    result = N1 - N2
    if result % 2 == 0:
        final = f"{N1} {operator} {N2} = {result} - even"
    else:
        final = f"{N1} {operator} {N2} = {result} - odd"
elif operator == "*":
    result = N1 * N2
    if result % 2 == 0:
        final = f"{N1} {operator} {N2} = {result} - even"
    else:
        final = f"{N1} {operator} {N2} = {result} - odd"

elif operator == "/" and N2 == 0 or (operator == "%" and N2 == 0):
    print(f"Cannot divide {N1} by zero")

elif operator == "/":
    result = N1 / N2
    final = f"{N1} / {N2} = {result:.2f}"

else:
    result = N1 % N2
    final = f"{N1} % {N2} = {result:}"

print(final)
