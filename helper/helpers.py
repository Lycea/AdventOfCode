import os
import io

def parse_by_next_new_line_array(array):
    stack =[]
    ret_items=[]
    #print(array)
    for item in array:
        #print(item)
        if item.strip() =="":
            #print("only new line")
            #print(stack)
            ret_items.append(stack)
            stack = []
        else:
            stack.append(item.strip())

    if len(stack)!= 0:
        ret_items.append(stack)

    #print("Found stacks:",len(ret_items))
    #print(ret_items)
    #print("\n")
    return ret_items


def parse_by_nex_new_line(array):
    stack =""
    ret_items=[]
    #print(array)
    for item in array:
        #print(item)
        if item.strip() =="":
            #print("only new line")
            #print(stack)
            ret_items.append(stack)
            stack = ""
        else:
            stack+=" "+item.strip()

    if len(stack)!= 0:
        ret_items.append(stack)

    #print("Found stacks:",len(ret_items))
    #print("\n".join(ret_items))
    #print("\n")
    return ret_items

def split_array_line_by(array,splitter):
    ret_items =[]
    
    for item in array:
        ret_items.append( item.split(splitter) )
    return ret_items

def remove_spaces(array):
    idx = 0
    for row in array:
        array[idx]=row.strip().replace(" ","")
        idx+=1

    return array

#converts an array of numbers into an array of strings
def lines_to_nums(array):
    #print("turning given lines to numbers...")
    num_input =[]
    #print(array)
    for line in array:
        num_input.append(int(line))
    #print(num_input)
    return num_input

def line_to_words(array):
    #print("splitting line to its under 'words'")
    word_lines=[]
    for line in array:
        word_lines.append(line.split(" "))

    return word_lines

#gets the input line by line
def get_input(file_name):
    input=[]
    #print("getting the input from the named file...")
    if os.path.exists(file_name):
        with open(file_name,"r") as fh:
            input = [x.strip() for x in fh.readlines()]
    else:
        print("WARNING: File could not be found")

    return input



class Input():
    def __init__(self,real_input=False):
        if real_input:
            self._data = get_input("input.input")
        else:
            self._data = get_input("sample.input")
    
    def get(self):
        return self._data

    def set(self, array):
        self._data = array
        return self

    def to_word(self):
        self._data = line_to_words(self._data)
        return self
   
    def to_number(self):
        self._data = lines_to_nums(self._data)
        return self
    
    def strip(self):
        self._data = remove_spaces(self._data)
        return self

    def split_chunks(self):
        self._data = parse_by_next_new_line_array(self._data)
        return self
    
    def split_by(self, splitter):
        self._data = split_array_line_by(self._data, splitter)
        return self

if __name__ == "__main__":
    print( Input().to_word().get() )


