s = input()
temp=[]
res=''
for i in range(len(s)):
    if(s[i] not in temp):
        temp.append(s[i])
for i in range(len(temp)-1,-1,-1):
    res+=temp[i]
print(res)
