import sys

f = sys.stdin.readline()

plus, minus, mysum = 0, 0, 0
temp = 0
num = ''

for idx, substr in enumerate(f):
    # print(substr, mysum, idx)

    if minus==1:
        if substr == '+':
            temp += int(num)
            num = ''
        elif substr == '-':
            if temp != 0:
                temp += int(num)
                mysum -= temp
                temp = 0
            else:
                mysum -= int(num)
            num = ''
        else:
            num+=substr
    else:
        if substr == '+':
            mysum += int(num)
            num = ''
        elif substr == '-': 
            minus = 1
            mysum += int(num)
            num = ''
        else:
            num+=substr
    
    if idx==len(f)-1:
        if minus==1:
            mysum -= (temp+int(num))
        else:
            mysum +=int(num)

print(mysum)

# + + -> 
# + - -> 
# - + ->
# - - ->

## 1-2+3-4+5-6+7-8+9
## 1-5-9-13-17=-43

## 55-50+40
## 55-90=-35