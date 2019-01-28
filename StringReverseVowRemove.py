n = int(input())
s = input()
vow = ['a','e','i','o','u']
res=''
temp = []
for i in range(len(s)):
    if(s[i] not in vow):
        temp.append(s[i])
for i in range(len(temp)-1,-1,-1):
    res+=temp[i]
print(res)
