n = int(input())
n1=n2=n
c,res=0,0
while n>0:
  c+=1
  n//=10
  
while n1>0:
   r=n1%10
   res=res+int(pow(r,c))
   n1//=10
  
if res==n2:
    print("Armstrong")
else:
    print("Not Armstrong")
