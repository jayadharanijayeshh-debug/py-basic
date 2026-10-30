a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

avg = (a + b + c + d + e) / 5

if avg >= 90:
    print("Excellent!")
elif avg >= 80:
    print("Great Job!")
elif avg >= 70:
    print("Good Effort!")
elif avg >= 50:
    print("Keep Trying!")
else:
    print("Better Luck Next Time!")
