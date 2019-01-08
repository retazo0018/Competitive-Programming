n  = int(input())
nn = input()
li2=[]
temp=[]
li = list(map(int, nn.split()))
for i in li:
    if(i not in li2):
        li2.append(i)
for i in range(len(li2)):
    if(li.count(li2[i])>1):
        temp.append(li.count(li2[i]))
if(len(temp)==0):
    print("unique")
else:
    print(sorted(temp))
