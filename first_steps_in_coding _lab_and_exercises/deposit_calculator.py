deposit = float(input())
deposit_term_in_months = int(input())
yearly_percent = float (input()) / 100

total = deposit + deposit_term_in_months * ((deposit * yearly_percent) / 12)

print({total})