import sys

T = int(sys.stdin.readline())
f = [1 for i in range(T)]
zero = 0
one = 1

if(T==0):
    print(zero)
elif(T==1 or T==2):
    print(one)
else:
    for i in range(2, T, 1):
        f[i] = f[i-2] + f[i-1]
    print(f[T-1])