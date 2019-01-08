s = input()
li = s.split()
li2 = []
x=1
flag=0
res=''
for i in range (len(li)):
    li2.append(li[i][0].upper())
res+=li2[0]
for i in range(len(s)):
    if(s[i]==" "):
        flag=1
        res+=" "
    if(flag==1):
        res+=li2[x]
        x+=1
        flag=0
    elif(flag==0 and s[i-1]!=" " and i!=1):
        res+=s[i]
print(res)
