n=int(input())
n1=n
res=0
while n>0:
  r=n%10
  f=1
  for i in range(1,r+1):
    f=f*i
  res=res+f
  n//=10
  
if res==n1:
    print("Strong")
else:
    print("Not Strong")
