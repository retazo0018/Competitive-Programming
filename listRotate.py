from collections import deque
n,k = map(int,input().split())
li = deque(list(map(int,input().split())))
for i in range(k):
    li.rotate(1)
for i in range(len(li)-1):
    print(li[i],end=" ")
print(li[len(li)-1])
