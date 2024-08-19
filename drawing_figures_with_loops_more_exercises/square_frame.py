n = int(input())

for row in range(1,n+1):
    if row == 1 or row == n:
        print("+ " + "- " * (n - 2) + "+ ")
        for col in range(n - 2):
            print("| " + "- " * (n - 2) + "| ")


