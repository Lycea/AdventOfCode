from helper.helpers import  *
from queue import LifoQueue
import io

input_=""
movement_lists =[]
cointainer_stacks =[]
num_containers = 0


def parse():
    global input
    global movement_lists
    global num_containers
    global cointainer_stacks

    input_=Input(real_input=True ,stripped=False).split_chunks()

    input_parsed=input_.get()
    
    list_containers = input_parsed[0]
    list_movements  = input_parsed[1]

    #movements
    print("parsing movements")
    for move in list_movements:
        splitted = move.strip().split(" ")
        movement_lists.append([int(splitted[1]),int(splitted[3]) - 1,int(splitted[5]) -1])
    print(movement_lists)
    print("\nparsing containers...")
    #getting number of containers
    num_containers = int(list_containers[-1].split("  ")[-1].strip())

    for item in range(num_containers):
        cointainer_stacks.append(LifoQueue())
    print(cointainer_stacks)

    print("containers to parse:",num_containers)
    import math
    #parsing containers
    for row in reversed( list_containers[:-1] ):
        #print("\nSTARTING ROW")
        #print(row)
        split = row.split( " ")
        print(split)
        space_since_last_container = 0
        last_index = 0

        for idx, tok in enumerate(split):
            
            if tok.strip() == "":
                space_since_last_container+=1
            else:
        
                
                #this is the first container
                if space_since_last_container == 0 and idx == 0:
                    pass
                elif space_since_last_container < 2:
                    last_index+=1
                else:
         #           print(f"space since last {space_since_last_container} ")
                    last_index+= math.ceil(space_since_last_container/4)
         #       print(" Adding to stack:",last_index)

                print("\n  ",tok,space_since_last_container,last_index)

                cointainer_stacks[last_index].put(tok[1])

                space_since_last_container=1

    for stack in cointainer_stacks:
        print(list(stack.queue))
                
        


    
def do():
    parse()

    global cointainer_stacks
    print("starting run")
    for movement in movement_lists:
        #print("\n"+("="*10))
        #print("Move")
        #print(movement)
        for _ in range(movement[0]):
            #print("...")
            if cointainer_stacks[movement[1]].empty() is False:
                poped_elem = cointainer_stacks[movement[1]].get(False,None)
                cointainer_stacks[movement[2]].put(poped_elem)
            else:
                print("empty ??")

        #print("\nStack infos:")

    word=""
    for stack in cointainer_stacks:
        word+=stack.get()

    print(word)
    print("")
            


def run():  
    print("\n\ns1")
    do()

    


