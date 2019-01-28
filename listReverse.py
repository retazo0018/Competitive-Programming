n = int(input())
li = list(map(int,input().split()))
for i in range(len(li)-1,0,-1):
  print(li[i],end="")
  print("->",end="")
print(li[0],end="")
