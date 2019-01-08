a,b = input().split()
a = a.lower()
b = b.lower()
temp1 = []
temp2 = []
ch=0
for i in range(len(a)):
    if(a[i] not in temp1):
        temp1.append(a[i])
for i in range(len(b)):
    if(b[i] not in temp2):
        temp2.append(b[i])
for i in range(len(temp1)):
    if(temp1[i] in temp2):
        ch+=1
if(ch==max(len(temp1),len(temp2))-1):
    print("yes")
else:
    print("no")
