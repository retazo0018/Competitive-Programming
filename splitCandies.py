n1 = int(input())
li = list(map(int,input().split()))
re=0
flag=0
for j in range(n1):
  for i in range(len(li)):
    if(li[i]>=1):
      re+=1
    if(li[i]>0):
      li[i]-=1
    ze = li.count(0)
  if(ze==len(li)-1):
    flag=1
    break
if(flag==1):
  print(re+1)
else:
  print(re)
