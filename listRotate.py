from collections import deque
n,k = map(int,input().split())
li = deque(list(map(int,input().split())))
for i in range(k):
    li.rotate(1)
for i in li:
    print(i,end=" ")
