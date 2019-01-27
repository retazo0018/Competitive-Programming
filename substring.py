s = input()
c=1
tot=0
for i in range(1,len(s)):
    if(s[i]==s[i-1]):
        c+=1
        if(i == len(s)-1):
            if(c>tot):
                tot = c
                ch = s[i-1]
    else:
        if(c>tot):
            tot = c
            ch = s[i-1]
        c=1
print(ch,tot)
