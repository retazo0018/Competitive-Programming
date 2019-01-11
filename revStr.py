s=input()
res=''
for i in s.split():
    res+=i[::-1]
    res+=" "
res=res.strip()
print(res)
