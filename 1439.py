
import sys

S = sys.stdin.readline()
Z, O, idx = 0, 0, 0
isall = True

for s in S:

    if idx==0:
        if s=='0':
            zero, one, idx = 1, 0, -1
            Z += 1
        elif s=='1':
            zero, one, idx = 0, 1, -1
            O += 1
    else:
        if zero==0 and one==1 and s=='1':
            continue
        if zero==0 and one==1 and s=='0':
            zero, one, isall = 1, 0, False
            Z += 1
        if zero==1 and one==0 and s=='1':
            zero, one, isall = 0, 1, False
            O += 1
        if zero==1 and one==0 and s=='0':
            continue

if isall:
    print('0')
else:
    if min(Z, O) == 0:
        print('1')
    else:
        print(min(Z, O))


