from helper.helpers import  *

input=""




def run():
    global input
    print("s1")
    input=get_input("real_input.input")

    last_number = 0
    increases   = 0

    dephs =lines_to_nums(input)

    for number in range(0,len(dephs)):
        if number !=  0:
            if dephs[number] >last_number:
                increases+=1

        last_number = dephs[number]


    print(increases)
    print("-"*30)
    print("done")
    print("-"*30)


