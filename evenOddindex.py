n = int(input())
li = list(map(int,input().split()))
result=[]
x=0
for i in range(len(li)):
    if(li[i]%2!=0 and x%2==0):
        result.append(li[i])
    elif(li[i]%2==0 and x%2!=0):
        result.append(li[i])
    x+=1
for i in range (len(result)):
    if(i==len(result)-1):
        print(result[i])
    else:
        print(result[i],end=" ")
