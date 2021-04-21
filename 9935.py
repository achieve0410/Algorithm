
# CC44mirkovC4niz
# C4

p_str = str(input())
b_str = str(input())

b_len = len(b_str)
temp = 0
temp_str = ''
temp_idx = 0

myarray = [0 for _ in range(len(p_str))]
my_str = []

answer = ''

for idx, value in enumerate(p_str):
    # print(idx, value)

    # print("temp")
    # print(temp, temp_str, temp_idx)

    # print("answer: ", answer)
    # print("temp_str: ", temp_str)
    # print("idx: ", idx)

    if b_str == temp_str+value and idx!=len(p_str)-1:
        # print("##########################")
        # print("answer: ", answer)
        # print("temp_str: ", temp_str)
        # print("idx: ", idx)

        my_str.append(idx)

        for my in my_str:
            # print(my)
            myarray[my] = 1
        
        # print("myarray: ", myarray)

        temp, temp_idx, temp_str = 0, 0, ''
        c_num = 0
        c_temp = 0
        ## check

        for i in range(b_len*2, b_len-1, -1):
            # print("i", idx-i)
            if idx-i>=0:
                # print(p_str[idx-i], b_str[c_num])
                if myarray[idx-i] == 0:
                    if p_str[idx-i] == b_str[0]:
                        if c_temp == 1:
                            temp_str = p_str[idx-i]
                            c_num = 1
                            c_temp = 1

                            my_str.append(idx-i)

                            temp, temp_idx= 1, 1
                        else:
                            temp_str = p_str[idx-i]
                            c_num += 1
                            c_temp = 1

                            my_str.append(idx-i)

                            temp, temp_idx = 1, temp_idx+1

                    elif p_str[idx-i] == b_str[c_num]:
                        temp_str += p_str[idx-i]
                        c_num += 1
                        
                        my_str.append(idx-i)

                        temp, temp_idx = 1, temp_idx+1

                    else:
                        temp, temp_idx, temp_str = 0, 0, ''
                        c_temp = 0

                        my_str = []
            else:
                continue
        # print(answer, c_num)
        answer = answer[:len(answer)-temp_idx]
        # print(answer)
        # print(temp_str)
        continue

    if temp == 0:
        # print("!")
        if value == b_str[temp_idx]:
            temp = 1
            temp_idx += 1
            temp_str += value
            my_str.append(idx)
            # print(temp_str)
        else:
            answer += value
            continue 
    else:
        # print("@")
        if value == b_str[temp_idx]:
            # print("#")
            # temp = 1
            temp_idx += 1
            temp_str += value
            my_str.append(idx)
        
        elif value == b_str[0]:
            # print("$")
            answer += temp_str
            temp = 1
            temp_idx = 1
            temp_str = value

            my_str = [idx]

        else:
            # print("%")
            temp_str += value
            answer += temp_str
            temp, temp_idx, temp_str, my_str = 0, 0, '', []
    

if answer == '':
    print('FRULA')
else:
    print(answer)
            






