from helper.helpers import  *

input=""



def parse():
    global input
    input=Input(False).get()
    
def do():
    parse()

    all_wrong_value = 0
    for line in input:
        half_size = int(len(line)/2)

        half1 = line[:half_size]
        half2 = line[half_size:]

        #print(half1)
        #print(half2)

        counter_items_1 = {}
        counter_items_2 = {}

        half1 = set(half1)
        half2 = set(half2)

        #print(half1)
        #print(half2)
        same_items = half1.intersection(half2)
        item = list(same_items)[0]
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

        #print(ord(item))

    print(f"wrong value of all: {all_wrong_value}")    
        
def run():  
    print("\n\ns1")
    do()

    


