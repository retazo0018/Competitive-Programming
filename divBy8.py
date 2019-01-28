def recur(n):
    if(n%8==0):
        return True
    else:
        return False
n = int(input())
res=''
flag=0
li = list(str(n))
for i in range(len(li)):
    res+=li[i]
    if(recur(int(res))):
        flag=1
    res=''
    for j in range(i,len(li)):
        res+=li[j]
        if(recur(int(res))):
            flag=1
    res=''
if(flag==0):
    print("no")
else:
    print("yes")
