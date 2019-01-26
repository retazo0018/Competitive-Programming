n = int(input())
li = []
c=0
for i in range(n):
    temp = input()
    li.append(temp.split())
for i in range(len(li)):
    c+=li[i].count('1')
if(c==1):
    print(1)
else:
    print(0)
