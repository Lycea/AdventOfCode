from helper.helpers import  *

input=""

class clean_set():
    def __init__(self, set_range) -> None:
        self._input = set_range
        self.set_length = 0
        self.set_start = 0
        self.set_end = 0
        self.stringifyed =  ""

        splitted_nums = self._input.split("-")
        self.set_end = int(splitted_nums[1])
        self.set_start = int(splitted_nums[0])
        self.set_length = self.set_end -self.set_start
        self.set_range = list(range(self.set_start,self.set_end+1))

        self.inside = False
        #print(self.set_range)

    def __str__(self):
        return f"{self.set_length}"
        

    def contains(self,set_b):
        if set_b.set_start in self.set_range and set_b.set_end in self.set_range and set_b.inside ==False:
            print("set is within")
            print("   ",self._input)
            print("   ",set_b._input)
            set_b.inside = True
            return True
        else:
            return False
            

def parse():
    global input
    input=Input(True).split_by(",").get()
    print(input)
    

def do():
    parse() 
    found_containments = 0
    for clean_sets in input:
        pair_sets = []
        for set_ in clean_sets:
            pair_sets.append(clean_set(set_))
        
        if pair_sets[0].contains(pair_sets[1]):
            found_containments+=1
            continue
            
        if pair_sets[1].contains(pair_sets[0]):
            found_containments+=1
            continue
    
    print("Full overlaps:",found_containments)


def run():  
    print("\n\ns1")
    do()

    


