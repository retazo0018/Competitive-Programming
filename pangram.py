s = input()
s = s.lower()
temp=[]
for i in range(len(s)):
  if(s[i] not in temp and s[i]!=' '):
    temp.append(s[i])
if(len(temp)==26):
  print("yes")
else:
  print("no")
