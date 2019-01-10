n = int(input())
li = list(map(int,input().split()))
res=[]
x=0
for i in range(len(li)):
    if(li[i]%2!=0 and x%2==0):
        res.append(li[i])
    elif(li[i]%2==0 and x%2!=0):
        res.append(li[i])
    x+=1
for i in range (len(res)):
    if(i==len(res)-1):
        print(res[i])
    else:
        print(res[i],end=" ")
