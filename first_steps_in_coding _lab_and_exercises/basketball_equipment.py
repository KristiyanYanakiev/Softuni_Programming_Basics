yearly_fee = int(input())

sneakers = yearly_fee - yearly_fee * 0.40
wear = sneakers - sneakers * 0.20
ball = wear / 4
accessories = ball / 5

total = yearly_fee + sneakers + wear + ball + accessories

print(total)