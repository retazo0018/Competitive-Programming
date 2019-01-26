s = input()
flag=0
le=0
c=1
for i in range(len(s)-1):
    if(s[i]==s[i+1]):
        c+=1
    else:
        if(c>le):
            char = s[i]
            le = c
        c=1
print(char,le)
