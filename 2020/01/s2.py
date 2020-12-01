from helper.helpers import *


input = ""




def find_2020():
    num_list=lines_to_nums(input)

    #sort the list
    num_list=sorted(num_list)
    print(num_list)

    for num in range(0,len(num_list)):
        print(num)
        first_num = num_list[num]
        for sec_num in range(len(num_list)-1,num,-1):
            second_num = num_list[sec_num]

            if second_num +first_num >=2020:
                print("to big already jump...",first_num,second_num,num,second_num)
                continue
            else:
                #go for the third loop, woho....
                for third_num in range(num,sec_num):
                    third_number = num_list[third_num]
                    if third_number+second_num+first_num == 2020:
                        print("\nFounnd")
                        print("FIRST",first_num)
                        print("SECOND",second_num)
                        print("THIRD",third_number)
                        print("\nRESULT:",first_num*second_num*third_number)
                        return
                    elif first_num+second_num+third_number>2020:
                        print("jumping,to big already", third_number + second_num + first_num, first_num, second_num, third_number)
                        break
                    else:
                        print("jumping, no fit",third_number+second_num+first_num,first_num,second_num,third_number)






def run():
    global input
    print("s2")
    input = get_input("real_input1.input")
    find_2020()