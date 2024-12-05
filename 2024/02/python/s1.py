from helper.helpers import  *

input_=""



def parse():
    global input_
    input_=Input(real_input=True)
    data = line_to_words(input_.get())

    for row_idx in range(0,len(data)) :
        data[row_idx] = [ int(single_num)  for  single_num in data[row_idx] ]
    input_ = data   


def check_distances(list_):
    #print(f"next {list_}")
    for num in range(len(list_)-1):
        dist_ = abs(list_[num] - list_[num+1])
        if dist_ > 0  and dist_ <= 3 :
            continue
        else:
            return False

    return True


def do():
    parse()
    valid_reps = 0

    for row in input_:
        is_sorted = False
        
        if sorted(row) == row:
            # print("is sorted")
            # print(row, sorted(row))
            is_sorted=True
            if check_distances(row):
                valid_reps+=1
        elif sorted(row,reverse=True) == row:
            # print("reverse sorted")
            # print(sorted(row,reverse=True),row)
            is_sorted=True
            if check_distances(row):
                valid_reps+=1
        else:
            pass
            #print("not sorted:",row)

    print(valid_reps)


def run():
    print("\n\ns1")
    do()

    


