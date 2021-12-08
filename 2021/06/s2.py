from helper.helpers import  *

input=""


def run():
    global input
    print("s2")
    #input=get_input("input.input")[0]

    input=get_input("real_input.input")[0]

    fishies= [int(x) for x in input.strip().split(",")]

    sorted_fishies =[0 for x in range(9)]
    sorted_fishies_new =[0 for x in range(9)]

    for fish in fishies:
        sorted_fishies[fish]+=1



    for i in range(256):
        print("Day ",i)

        print("start:",sorted_fishies)
        for idx in reversed(range(9)):
            if idx == 0 :
                sorted_fishies_new[6]+= sorted_fishies[idx]
                sorted_fishies_new[8]+= sorted_fishies[idx]
            else:
                sorted_fishies_new[idx - 1] += sorted_fishies[idx]

        sorted_fishies = sorted_fishies_new.copy()
        sorted_fishies_new = [0 for x in range(9)]

        print("end  :",sorted_fishies)

    print(sorted_fishies)
    print(sum(sorted_fishies))