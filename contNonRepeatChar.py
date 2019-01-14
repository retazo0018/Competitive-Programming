s = input()
li = list(s)
temp = []
res=0
ch=0
for i in range(len(li)):
    if(li[i] not in temp):
        temp.append(li[i])
    else:
        ch+=1
        t = len(temp)
        if(t>res):
            res = t
        temp=[]
if(ch==0):
    print(len(li))
else:
    print(res)
