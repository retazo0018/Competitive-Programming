n = int(input())
li = list(map(int,input().split()))
res=[]
c=1
m=0
for i in range(len(li)):
  if(i==(len(li)-1)):
    pass
  else:
    res.append(li[i+1]>=li[i])
for i in res:
  if(c>m):
      m=c
  if(i==True):
    c+=1
  else:
    c=1
if(c>m):
      m=c
print(m)
