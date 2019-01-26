a = input()
b = input()
res=''
for i in range(min(len(a),len(b))):
    if(a[i]==b[i]):
        res+=a[i]
    else:
        break
if(len(a)>=len(b)):
    tlen = len(a)
else:
    tlen = len(b)
print(tlen//len(res))
