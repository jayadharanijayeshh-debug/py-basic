n = int(input())
count = 0

if n == 0:
  count = 1 
else:
  while n > 0:
    digit = n % 10
    if digit == 0:
      count += 1 
    n = n // 10
    
print(count)
