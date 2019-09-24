import sys

N = int(sys.stdin.readline())
X = [0 for i in range(N)]

X_str = sys.stdin.readline().split()

for i in range(N+1):
    X[i] = int(X_str[i])