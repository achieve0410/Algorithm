import sys

def gcd(a, b):
    big = max(a,b)
    small = min(a,b)
    rmd = big%small

    while(True):
        # print("big: {}, small: {}, rmd: {}".format(big, small, rmd))
        if(rmd==0):
            return small
        else:
            big = small
            small = rmd
            rmd = big%small

n, k = map(int, sys.stdin.readline().split())
f = [1 for i in range(n+1)]
mySum = 0
mod = 1000000007

for i in range(2, n+1, 1):
    f[i] = f[i-2] + f[i-1]

for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):            
        f_arg = gcd(i, j)**k % mod
        s_arg = gcd(f[i-1], f[j-1]) % mod
        mySum += f_arg*s_arg

print(mySum%mod)