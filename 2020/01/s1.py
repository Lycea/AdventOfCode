
from helper.helpers import *


input = ""




def find_2020():
    num_list=lines_to_nums(input)

    #sort the list
    num_list=sorted(num_list)
    print(num_list)

    for num in range(0,len(num_list)):
       # print(num)
        first_num = num_list[num]
        for sec_num in range(len(num_list)-1,num,-1):
            #print(sec_num)
            second_num = num_list[sec_num]

            if second_num +first_num <2020:
                print("to small already jump...",first_num,second_num)
                break
            elif second_num+first_num == 2020:
                print("found")
                print(first_num,second_num,first_num*second_num)
                return
            else:
                print("continueing... not found yet",first_num,second_num)
                continue



def run():
    global input
    print("-----------")
    print("starting s1")

    input = get_input("real_input1.input")
    find_2020()
    print("the output should be correct!!!")
    print("-----------")