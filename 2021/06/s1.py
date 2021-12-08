from helper.helpers import  *

input=""




def run():
    global input
    print("s1")
    input=get_input("real_input.input")[0]

    fishies= [int(x) for x in input.strip().split(",")]

    for i in range(80):
        print("Day ",i)
        print("Fishies", len(fishies))
        #print(fishies)
        for fish_id in range(len(fishies)):
            if fishies[fish_id] == 0:
                fishies.append(8)
                fishies[fish_id]=6
            else:
                fishies[fish_id]-=1


    print(len(fishies))