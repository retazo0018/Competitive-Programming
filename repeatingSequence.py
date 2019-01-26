n = int(input())
li = list(map(int,input().split()))
c=1
re=[]
for i in range(len(li)):
    for j in range(i,len(li)-1):
        if(li[j]<0 and li[j+1]>0):
            c+=1
        elif(li[j]>0 and li[j+1]<0):
            c+=1
        else:
            break
    re.append(c)
    c=1
for i in range(len(re)-1):
    print(re[i],end=" ")
print(re[len(re)-1])
