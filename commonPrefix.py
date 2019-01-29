n = int(input())
li=[]
t=[]
x=0
res=''
flag=0
for i in range(n):
    li.append(input())
for j in range(len(li[0])):
    temp = li[0][j]
    for i in range(len(li)):
        if(li[i][j] == temp):
            x+=1
        else:
            flag=1
    if(flag==1):
            break
    if(x==len(li)):
        t.append(li[i][j])
        x=0
for k in range(len(t)):
    res+=t[k]
print(res)
