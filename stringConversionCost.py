x,y = map(str,input().split())
c = 0
c+=abs(len(y)-len(x))
if(len(x)<=len(y)):
    ma = y
    mi = x
else:
    ma = x
    mi = y
for i in range(len(mi)):
    if(mi[i]!=ma[i]):
        c+=1
print(c)
