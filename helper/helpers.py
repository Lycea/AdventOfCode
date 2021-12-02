import os
import io

def parse_by_next_new_line_array(array):
    stack =[]
    ret_items=[]
    print(array)
    for item in array:
        print(item)
        if item.strip() =="":
            print("only new line")
            print(stack)
            ret_items.append(stack)
            stack = []
        else:
            stack.append(item.strip())

    if len(stack)!= 0:
        ret_items.append(stack)

    print("Found stacks:",len(ret_items))
    print(ret_items)
    print("\n")
    return ret_items


def parse_by_nex_new_line(array):
    stack =""
    ret_items=[]
    print(array)
    for item in array:
        print(item)
        if item.strip() =="":
            print("only new line")
            print(stack)
            ret_items.append(stack)
            stack = ""
        else:
            stack+=" "+item.strip()

    if len(stack)!= 0:
        ret_items.append(stack)

    print("Found stacks:",len(ret_items))
    print("\n".join(ret_items))
    print("\n")
    return ret_items


def remove_spaces(array):
    idx = 0
    for row in array:
        array[idx]=row.strip().replace(" ","")
        idx+=1

    return array

#converts an array of numbers into an array of strings
def lines_to_nums(array):
    print("turning given lines to numbers...")
    num_input =[]
    print(array)
    for line in array:
        num_input.append(int(line))
    print(num_input)
    return num_input

def line_to_words(array):
    print("splitting line to its under 'words'")
    word_lines=[]
    for line in array:
        word_lines.append(line.split(" "))

    return word_lines

#gets the input line by line
def get_input(file_name):
    input=[]
    print("getting the input from the named file...")
    with open(file_name,"r") as fh:
        input = fh.readlines()


    return input