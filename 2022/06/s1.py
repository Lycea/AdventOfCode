from helper.helpers import  *

input=""



def parse():
    global input
    input=Input(True).get()
    
def do():
    parse()
    command_list = list(input[0])
    print("start")
    for last_index in range(4,len(command_list)):
        to_check = command_list[last_index-4:last_index]
        if len(list(set(to_check))) == 4:
            print(last_index)
            break


def run():  
    print("\n\ns1")
    do()

    


