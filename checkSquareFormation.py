x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
x4,y4 = map(int,input().split())
li1=[]
li2=[]
for i in (x1,x2,x3,x4):
    if(i not in li1):
        li1.append(i)
for i in (y1,y2,y3,y4):
    if(i not in li2):
        li2.append(i)
if(len(li1)==2 and len(li2)==2):
    print("yes")
else:
    print("no")
