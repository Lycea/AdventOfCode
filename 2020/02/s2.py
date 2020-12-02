from helper.helpers import  *

input=""

def run_check():
    print("starting iterating lines...")

    count_valid = 0
    valids =[]

    for line in input:

        line = line.strip().split(":")
        #print(line)

        code   = line[1].replace(" ","")
        policy = line[0].split(" ")
        char_to_check = policy[1]

        positions = policy[0].split("-")

        correct_idxes = 0

        for position in positions:
            if len(code)<int(position):
                print("to long place ... skipping pos",line)
                continue#silently ignore this position since it is out of range...
            elif code[int(position)-1] == policy[1]:
                correct_idxes+=1


        if correct_idxes == 1:
            count_valid+=1
            valids.append(line)

        #print("-"*10)

    print("Valid found:",count_valid)
    print(valids)






def run():
    global input
    print("-----------")
    print("starting s2")

    input = get_input("real_input.input")
    run_check()
    print("-----------")