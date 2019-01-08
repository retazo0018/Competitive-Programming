n  = int(input())
nn = input()
li2=[]
temp=[]
flag=0
li = list(map(int, nn.split()))
for i in range(len(li)):
    if(li[i] not in temp):
        temp.append(li[i])
    else:
        flag=1
        print(li[i])
        break
if(flag==0):
    print("unique")
