import sys

memo = {1:1, 2:1}

def fib(N):
    if(N==0):
        return 0
    if N not in memo:
        memo[N] = fib(N-1) + fib(N-2)
    return memo[N]

def fib_2(N):
    a, b = 1, 0
    for i in range(N):
        # print(i, a, b)
        a, b = b, a+b
    return b

N = int(sys.stdin.readline())
# print(fib(N))
print(fib_2(N))