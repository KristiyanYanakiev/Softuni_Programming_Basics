opened_tabs_number = int(input())
salary = int(input())


for _ in range(opened_tabs_number):
    site = input()
    if site == "Facebook":
        salary -= 150
    elif site == "Instagram":
        salary -= 100
    elif site == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(int(salary))