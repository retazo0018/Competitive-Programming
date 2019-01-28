n = int(input())
li = list(map(int,input().split()))
lia = sorted(li)
lid = sorted(li,reverse=True)
res=[]
if(len(li)%2==0):
    for i in range(len(li)//2):
        res.append(lid[i])
        res.append(lia[i])
    for i in range(len(res)-1):
        print(res[i],end=" ")
    print(res[len(res)-1])
else:
    for i in range(len(li)//2):
        res.append(lid[i])
        res.append(lia[i])
    res.append(lia[len(li)//2])
    for i in range(len(res)-1):
        print(res[i],end=" ")
    print(res[len(res)-1])
