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
    for number_pair in input_.get():
        list_team_a.append(int(number_pair[0]))
        list_team_b.append(int(number_pair[1]))

    list_team_a.sort()
    list_team_b.sort()

    sum_distances = 0
    for id_idx in range(len(input_.get())):
        sum_distances+= abs(list_team_a[id_idx]-list_team_b[id_idx] )

    print(f"sum: {sum_distances}")


def run():  
    print("\n\ns1")
    do()
