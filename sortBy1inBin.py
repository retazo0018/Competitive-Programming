n = int(input())
nn = input()
li = list(map(int,nn.split()))
li.sort(reverse=True)
arr = [(x,sum(list(map(int,bin(x)[2:])))) for x in li]
arr.sort(key=lambda x:x[1],reverse=True)
for i in range(len(arr)):
  print(arr[i][0])
