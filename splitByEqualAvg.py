def fun(li,sp):
    f=[]
    s=[]
    for i in range(len(li)):
        if(i<=sp):
            f.append(li[i])
        else:
            s.append(li[i])
    a1=0
    a2=0
    if(len(f)!=0):
        a1 = sum(f)//len(f)
    if(len(s)!=0):
        a2 = sum(s)//len(s)
    if(a1==a2):
        return True
    else:
        return False
n = int(input())
li = list(map(int,input().split()))
sp = len(li)//2
flag=0
while(fun(li,sp)==False):
    if(sp==0):
        flag=1
        break
    sp-=1
if(flag==1):
    print("no")
else:
    print("yes")
