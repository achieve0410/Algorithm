import sys

T = int(sys.stdin.readline())
f = [1 for i in range(T)]
one = 1
zero = 0

for i in range(2, T, 1):
    f[i] = f[i-2] + f[i-1]

for i in range(T):
    N = int(sys.stdin.readline())
    if(N==0):
        print(one, zero)
    elif(N==1):
        print(zero, one)
    else:
        print(f[N-2], f[N-1])