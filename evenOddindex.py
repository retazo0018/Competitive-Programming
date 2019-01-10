n = int(input())
li = list(map(int,input().split()))
res1=[]
res2=[]
x=0
y=0
for i in range(0,len(li),2):
    if(li[i]%2!=0):
        res1.append(li[i])
for i in range(1,len(li),2):
    if(li[i]%2==0):
        res2.append(li[i])
for i in range(len(li)):
    if(i%2==0 and x<len(res1)):
        print(res1[x],end=" ")
        x+=1
    elif(i%2!=0 and y<len(res2)):
        print(res2[y],end=" ")
        y+=1
