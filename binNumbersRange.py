def convert_int(number,decimals):
    return str(number).zfill(decimals)
n=int(input())
for i in range(2**n):
    print(convert_int(int(bin(i)[2:]),n))
