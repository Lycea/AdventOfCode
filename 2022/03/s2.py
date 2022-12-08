from helper.helpers import  *

input=""


def parse():
    global input
    input=Input(True).get()
    
def do():
    parse()

    all_wrong_value = 0
    group_lines =[]
    

    for line in input:
        
        group_lines.append(line)
        
        if len(group_lines)==3:
            sets = []
            for elve in group_lines:
                sets.append(set(list(elve)))
   
            same_items_first_parts = sets[0].intersection(sets[1])
            same_items_second_part = set(same_items_first_parts).intersection(sets[2])
            
            print(same_items_first_parts)
            print(same_items_second_part)
            
            item = list(same_items_second_part)[0]
            #print("Wrong item:",item)

            value = -1
            if item.isupper():
                offset = -38
                value = ord(item) + offset
                
            else:
                offset = -96  #from asci code back to 
                #print("low")
                value = ord(item) + offset
                
            all_wrong_value += value

            group_lines.clear()
            #print(ord(item))

    print(f"wrong value of all: {all_wrong_value}")   

def run():  
    print("\n\ns2")
    do()