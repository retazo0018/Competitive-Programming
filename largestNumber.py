n = int(input())
nn = input()
res=''
li= list(map(int, nn.split()))
li.sort(reverse=True)
for i in range(len(li)):
    res+=str(li[i])
print(int(res))
