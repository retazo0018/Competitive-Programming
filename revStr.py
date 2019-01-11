s=input()
res=''
for i in s.split():
    res+=i[::-1]
    res+=" "
print(res)
