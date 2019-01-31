r,c = map(int,input().split())
li=[]
for i in range(r):
    temp = list(map(int,input().split()))
    li.append(sorted(temp))
li.sort()
for i in range(r):
  for j in range(c):
    print(li[i][j],end=" ")
  print()
