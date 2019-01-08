n = int(input())
nn = input()
temp=[]
li= list(map(int, nn.split()))
for i in range(len(li)):
    if(i==li[i]):
        temp.append(li[i])
if(len(temp)==0):
    print(-1)
else:
    temp.sort()
    for i in range(len(temp)):
        if(i==len(temp)-1):
            print(temp[i])
        else:
            print(temp[i],end=" ")
