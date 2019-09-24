# import sys

# def calcMinDist(N, M, J):

#     box_left = 1
#     box_right = M
#     apple = J

#     count = 0

#     while apple:
#         loc = apple.pop(0)
#         if( loc < box_left ):
#             count += (box_left-loc)
#             box_left = loc
#             box_right = loc+(M-1)
#         elif( loc > box_right ):
#             count += (loc-box_right)
#             box_right = loc
#             box_left = loc-(M-1)
#         else:
#             continue
#     return count

# def main():

#     N, M = map(int, sys.stdin.readline().split())

#     J = []

#     for i in range(int(sys.stdin.readline())):
#         j = int(sys.stdin.readline())
#         J.append(j)

#     result = calcMinDist(N, M, J)
#     print(result)

# if( __name__ == '__main__'):
#     main()

import sys

N, M = map(int, sys.stdin.readline().split())

J = []

for i in range(int(sys.stdin.readline())):
    j = int(sys.stdin.readline())
    J.append(j)

box_left = 1
box_right = M

count = 0
while J:
    loc = J.pop(0)
    if( loc < box_left ):
        count += (box_left-loc)
        box_left = loc
        box_right = loc+(M-1)
    elif( loc > box_right ):
        count += (loc-box_right)
        box_right = loc
        box_left = loc-(M-1)
    else:
        continue
print(count)