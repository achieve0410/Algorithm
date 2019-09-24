# import sys

# def calcDiff(A, B):

#     minCount = 51
#     diff = len(B) - len(A)

#     for i in range(diff+1):
#         count = 0
#         for j in range(len(A)):
#             if( A[j] != B[i+j] ):
#                 count += 1
#         if( minCount > count ):
#             minCount = count
    
#     return minCount

# def main():

#     A, B = sys.stdin.readline().split()

#     result = calcDiff(A, B)
#     print(result)


# if(__name__ == "__main__"):
#     main()


import sys

A, B = sys.stdin.readline().split()

minCount = 51
diff = len(B) - len(A)

for i in range(diff+1):
    count = 0
    for j in range(len(A)):
        if( A[j] != B[i+j] ):
            count += 1
    if( minCount > count ):
        minCount = count

print(minCount)