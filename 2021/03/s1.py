from helper.helpers import  *

input=""




def run():
    global input
    print("s1")
    input=get_input("input.input")

    num_lines = len(input)
    counts = []

    gamma   = ""
    epsilon = ""
    for i in range(len(input[0].strip())):
        counts.append({"1":0,"0":0})


    for line in input:
        for num in range(len(line.strip())):
            counts[num][line[num]]+=1

    print(counts)

    for col in counts:
        if col["0"]> col["1"]:
            gamma += "0"
            epsilon +="1"
        else:
            gamma += "1"
            epsilon +="0"

    print(gamma,epsilon)
    g_num = int(gamma,2)
    e_num = int(epsilon,2)
    print(g_num,e_num,g_num*e_num)

    print(list(range(0,5)))