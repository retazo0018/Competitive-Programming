n = int(input())
c=0
for i in range(1,n):
  for j in range(i,n+1):
    if(i!=j):
      c+=1
print(c)
