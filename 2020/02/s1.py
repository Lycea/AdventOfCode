from helper.helpers import  *

input=""

def run_check():
    print("starting iterating lines...")

    count_valid = 0
    valids =[]

    for line in input:

        line = line.strip().split(":")
       # print(line)

        code   = line[1]
        policy = line[0].split(" ")
        char_to_check = policy[1]

        limits = policy[0].split("-")

        counted_chars = code.count(char_to_check)

        if counted_chars >=int(limits[0]) and counted_chars<=int(limits[1]):
            print("valid:",line)
            valids.append(code)
            count_valid+=1
        #print("-"*10)

    print("Valid found:",count_valid)
    print(valids)






def run():
    global input
    print("-----------")
    print("starting s1")

    input = get_input("real_input.input")
    run_check()
    print("-----------")