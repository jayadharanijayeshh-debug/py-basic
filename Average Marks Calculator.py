a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

avg = (a + b + c + d + e) / 5

if avg == int(avg):
    print(int(avg))
else:
    print(f"{avg:.2f}")
