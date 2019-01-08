l,r = input().split()
li = []
c=0
l = int(l)
r = int(r)
for i in range(l,r+1):
    for j in range(1,i+1):
        if(i%j==0):
            c+=1
    if(c==2):
        li.append(i)
    c=0
print(len(li))
