def convert_int(number,decimals):
    return str(number).zfill(decimals)
n=int(input())
li=[]
x=0
for i in range(2**n):
    temp = convert_int(int(bin(i)[2:]),n)
    li.append(temp)
print(li)
for j in range(len(li)):
    for i in range(len(li)):
        if(li[i].count('1')==x):
            print(li[i])
    x+=1
