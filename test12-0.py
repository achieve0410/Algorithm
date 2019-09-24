import sys

N = int(sys.stdin.readline())
X = sys.stdin.readline().split()
Y = [0 for i in range(N)]
Z = [0 for i in range(N+1)]

index = 0
for i in X:
    if (i == '<'):
        Y[index] = 1
    index += 1

cur = -1
cnt = 0
hnum = 9
for i in range(0, N):
    if(Y[i] == 1):
        cnt += 1
    else:
        if(cnt == 0):
            Z[i] = hnum
            hnum -= 1
        else:
            for j in range(i - cnt, i + 1):
                Z[j] = hnum - i + j
            hnum = hnum - cnt - 1
            cnt = 0
    

if(hnum > Z[i+1]):
    Z[i+1] = hnum

print(Z)
