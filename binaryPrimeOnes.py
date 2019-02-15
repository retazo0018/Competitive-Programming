a,b = map(int,input().split())
no=0
for i in range(a,b+1):
  bi = (bin(i)[2:])
  ones = bi.count('1')
  if(ones==2):
    pass
  elif(ones==1):
    no+=1
  else:
    for j in range(2,ones):
      if(ones%j==0):
        no+=1
print((abs(a-b)+1)-no)
