n = int(input())
li = [[0]*(n+2),[0]*(n+2)]
print(li)
c=0
for i in range(n):
  li.insert(-1,[0]+[int(x) for x in input().split()]+[0])
for i in range(1,n+1):
  for j in range(1,n+1):
    if(li[i][j]==1 and [[[li[i-1][k],li[i][k],li[i+1][k]]for k in range(j-1,j+2)]==[0,0,0],[0,1,0],[0,0,0]]):
      c+=1
print(c)
