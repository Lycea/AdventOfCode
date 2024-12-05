from helper.helpers import  *

input_=""


def parse():
    global input_
    input_=Input(real_input=True).split_by("   ")
    
def do():
    parse()
    #print(input_.get())

    list_team_a = []
    list_team_b = []

    number_index = {}

    for number_pair in input_.get():
        if  number_pair[0] not in number_index:
            number_index[number_pair[0]]={
                "found_right": 0,
                "found_left": 1
            }
        else:
            number_index[number_pair[0]]["found_left"]+=1

        #list_team_a.append(int(number_pair[0]))
        list_team_b.append(number_pair[1])


    for number in list_team_b:
        if number in number_index:
            number_index[number]["found_right"]+=1
        else:
            print(f"Number not found in index {number}")

    #print(number_index)
    similarity = 0
    for index in number_index:
        similarity+= (number_index[index]["found_left"]* number_index[index]["found_right"])*int(index)
#        similarity+= (number_index[index]["found_left"]* number_index[index]["found_right"])

    print(f"similarity: {similarity}")

def run():  
    print("\n\ns2")
    do()
