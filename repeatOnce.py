n = int(input())
nn = input()
temp=[]
li= list(map(int, nn.split()))
for i in range(len(li)):
    if(li.count(li[i])==1):
        print(li[i])
