r,c = map(int,input().split())
li=[]
t=[]
res=[]
for i in range(r):
    temp = list(map(int,input().split()))
    li.append(sorted(temp))
for i in range(c):
  for j in range(r):
    t.append(li[j][i])
  res.append(sorted(t))
  t=[]
for i in range(r):
  for j in range(c):
    print(res[j][i],end=" ")
  print()
  
