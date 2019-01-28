s = input()
flag=0
msd = ['d','h','o','n','i']
for i in range(len(s)):
    if(s[i] not in msd or msd.count(s[i])!=s.count(msd[i])):
        flag=1
        break
if(flag==0):
    print("yes")
else:
    print("no")
