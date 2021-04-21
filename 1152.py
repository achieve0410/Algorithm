import sys

mystr = list(input().split(" "))
num = 0

print(mystr)

for substr in mystr:
    if substr != "":
        num+=1

print(num)

