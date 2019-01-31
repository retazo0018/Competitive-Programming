r,c = map(int,input().split())
li=[]
for i in range(r):
    temp = list(map(int,input().split()))
    li.append(sorted(temp))
print(sorted(li))
