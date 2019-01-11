n = int(input())
li = list(map(int,input().split()))
res=0
flag=0
for j in range(n):
  for i in range(len(li)):
    if(li[i]>=1):
      res+=1
    if(li[i]>0):
      li[i]-=1
    ze = li.count(0)
  if(ze==len(li)-1):
    flag=1
    break
if(flag==1):
  print(res+1)
else:
  print(res)
