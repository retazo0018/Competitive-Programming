s = input()
eve = []
odd = []
y=0
res = ''
z=0
for i in range(0,len(s),2):
  eve.append(s[i])
for j in range(1,len(s),2):
  odd.append(s[j])
for k in range(len(s)):
  if(k%2!=0):
    res+=eve[y]
    y+=1
  else:
    res+=odd[z]
    z+=1
print(res)
