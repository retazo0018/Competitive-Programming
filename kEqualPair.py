n,k = input().split()
n = int(n)
flag=0
li = []
k = int(k)
nn = input()
li = list(map(int,nn.split()))
for i in range(len(li)):
    for j in range(len(li)):
        if(li[i]+li[j]==k):
            flag=1
            break
if(flag==0):
    print("no")
else:
    print("yes")
