def convert_int(number,decimals):
    return str(number).zfill(decimals)
n=int(input())
for i in range(2**n):
    temp = convert_int(int(bin(i)[2:]),n)
    print(temp)
