units = float(input())

if units <= 50:
    bill = units * 1
elif units <= 150:
    bill = 50 + (units - 50) * 2
elif units <= 250:
    bill = 50 + 100 * 2 + (units - 150) * 3
else:
    bill = 50 + 100 * 2 + 100 * 3 + (units - 250) * 4

if bill > 150:
    bill = bill + bill * 0.20

if bill == int(bill):
    print(int(bill))
else:
    print(bill)
