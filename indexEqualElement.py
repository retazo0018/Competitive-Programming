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
    for i in sorted(temp):
        print(i,end=" ")
