from helper.helpers import  *

input=""


def run():
    global input
    print("s2")
    input=get_input("real_input.input")

    last_sum = 0
    increases = 0

    dephs = lines_to_nums(input)

    for number in range(0, len(dephs)):
        nums = dephs[number:number + 3]

        if number+3 > len(dephs):
            break

        count = sum(nums)#nums[0]+nums[1]+nums[2]
        if number != 0:
            if count >last_sum:
                increases+=1



        last_sum = count





    print(increases)
    print("-" * 30)
    print("done")
    print("-" * 30)