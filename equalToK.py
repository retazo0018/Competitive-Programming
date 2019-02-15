n,k = map(int,input().split())
li = list(map(int,input().split()))
flag=0
for i in range(len(li)-1):
  for j in range(i+1,len(li)):
    if(li[i]+li[j]==k):
      print("YES")
      flag=1
  if(flag==1):
    break
if(flag==0):
  print("NO")
