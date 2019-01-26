n = int(input())
c=0
flag=0
for i in range(n+1):
    if(i<10):
        c+=1
    else:
        temp = str(i)
        li = list(map(int,temp))
        for j in range(len(li)-1):
            if(abs(li[j]-li[j+1])==1):
                flag=1
            else:
                flag=0
                break
        if(flag==1):
            for j in range(1,len(li)):
                if(abs(li[j-1]-li[j])==1):
                    flag=1
                else:
                    flag=0
                    break
        if(flag==1):
            c+=1
print(c)
