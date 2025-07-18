'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two 
binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary 
representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

'''
def solution(N):
    # Implement your solution here
    # AND: N & 1: Find the rightmost or least significant bit.
    # N >>= 1: Shift bits to the right; Divides the number by 2.
    # Idea: Keep checking the rightmost bit after a rightshift and count the continuous 0's. The loop ends when right shift outputs a 0 which means the number cannot be further divided or shifted.
    res, cur_max, flag = 0,0,0
    while N > 0:
        if N & 1 == 1: # AND Operation
            flag += 1
            if flag == 2:
                res = max(res, cur_max)
                cur_max, flag = 0, 1
        else:
            if flag == 1:
                cur_max += 1
        N >>= 1 # Right Shift
    return res
