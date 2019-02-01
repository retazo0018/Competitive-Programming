a,b = input().split()
res=''
for i in range(len(a)):
  t = ord(a[i])+ord(b[i])
  res+=chr(t-96)
print(res)
