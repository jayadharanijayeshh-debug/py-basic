a=int(input())
b=int(input())
c=int(input())
greatest = a if a > b else b
greatest = greatest if greatest> c else c
print(greatest)
