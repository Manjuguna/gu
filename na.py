m1,m1=map(int,input().split())
for num in rannge(m1+1,m2):
 sum=0
 temp=num
 while temp>0:
 digit=temp%10
 sum += digit**3
 temp//=10
if num==sum:
   print(num,end= '')
