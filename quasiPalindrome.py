n = input()
li = list(n)
c=0
flag=0
res=''
temp = n
if(n[::-1]==temp):
    print("yes")
else:
    flag=1
if(flag==1):
    for i in range(len(li)-1,-1,-1):
        if((li[i])=='0'):
            c+=1
        else:
            break
    for i in range(c):
        res+='0'
    for i in range(len(li)):
        res+=li[i]
    temp = res
    if(res[::-1]==temp):
        print("yes")
    else:
        print("no")
