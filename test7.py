
def makeAllSame(S):

    rep = len(S)

    num_list = []
    zero_count = 0
    one_count = 0

    for i in range(rep):
        if ( i == 0 ):
            if (S[i] == '0'):
                num_list.append(0)
                state_num = 0
                zero_count += 1
            else:
                num_list.append(1)
                state_num = 1
                one_count += 1

        if(state_num == 0):
            if (S[i] == '0'):
                continue
            else:
                num_list.append(1)
                state_num = 1
                one_count += 1

        else:
            if (S[i] == '0'):
                num_list.append(0)
                state_num = 0
                zero_count += 1
            else:
                continue
    return min(one_count, zero_count)

def main():

    S = input()

    result = makeAllSame(S)
    print(result)

if( __name__ == '__main__' ):
    main()