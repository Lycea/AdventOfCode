from helper.helpers import  *

input=""



def count_1s(list,bit):
    count = 0
    one_list = []
    zero_list = []

    print(len(list))
    for num in range(len(list)) :
       # print(list[num])
        if list[num][bit] == "1":
            count+=1
            one_list.append(list[num])
        else:
            zero_list.append(list[num])

    return [count,one_list,zero_list]

def run():
    global input
    print("s2")
    input=get_input("real_input.input")

    num_lines = len(input)

    oxygen_rating=input.copy()
    co2_rating   =input.copy()

    #calc oxygen
    for num in range(len(input[0].strip())):
        print("start",oxygen_rating)
        output = count_1s(oxygen_rating,num)
        if output[0]>len(oxygen_rating)/2:
            oxygen_rating=output[1]
        elif output[0]<len(oxygen_rating)/2:
            oxygen_rating = output[2]
        else:
            oxygen_rating = output[1]

        print("stop", oxygen_rating)
        if len(oxygen_rating) == 1:
            break


    print(oxygen_rating[0].strip(),int(oxygen_rating[0],2))

    #calc c02
    for num in range(len(input[0].strip())):
        print(co2_rating)
        output = count_1s(co2_rating,num)
        if output[0]<len(co2_rating)/2:
            co2_rating=output[1]
        elif output[0]>len(co2_rating)/2:
            co2_rating = output[2]
        else:
            co2_rating = output[2]

        print(co2_rating)
        if len(co2_rating) == 1:
            break
    print(co2_rating[0],int(co2_rating[0],2))
    print("final number")
    print(int(co2_rating[0],2)*int(oxygen_rating[0],2))