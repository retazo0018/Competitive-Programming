s1 = input()
s2 = input()
li1 = []
li2 = []
for i in range(len(s1)):
  if(s1[i] not in li1):
    li1.append(s1[i])
  if(s2[i] not in li2):
    li2.append(s2[i])
if(len(li1)==len(li2)):
  print("yes")
else:
  print("no")
    
