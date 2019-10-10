import sys

N = int(sys.stdin.readline())
zero = 0
one = 1

if(N==0):
    print(zero)
elif(N==1 or N==2):
    print(one)
else: ## N = 3, 4, 5, 6, ...
    f = [1 for i in range(N)]
    for i in range(2, N, 1):
        f[i] = f[i-2] + f[i-1]
        if(f[i]>=1000000007):
            f[i] -= 1000000007

    print(f[N-1])