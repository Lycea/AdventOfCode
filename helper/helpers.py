import os
import io


def lines_to_nums(array):
    print("turning given lines to numbers...")
    num_input =[]
    print(array)
    for line in array:
        num_input.append(int(line))
    print(num_input)
    return num_input


def get_input(file_name):
    input=[]
    print("getting the input from the named file...")
    with open(file_name,"r") as fh:
        input = fh.readlines()

    return input
