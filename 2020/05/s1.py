from helper.helpers import  *
import math

input=""



def iterate_code(code,start,stop,lower_char,upper_char,div=2):
    start = start
    stop  = stop

    while code != "":
        dist = stop - start
        lower_idxs = [start, math.floor(start + dist / 2)]
        upper_idxs = [math.ceil(start + dist / 2), stop]

        #print("lower", lower_idxs)
        #print("upper", upper_idxs)

        #print(code)
        process_letter = code[0]

        if process_letter == lower_char:
            start = lower_idxs[0]
            stop = lower_idxs[1]
        else:
            start = upper_idxs[0]
            stop = upper_idxs[1]
        code = code[1:]

    #print(start,stop)
    return(start)

def check_rows():
    max_id = 0
    id_list = []

    for seat_code in input:
        #print(seat_code)
        row_code = seat_code[:7]
        place_code = seat_code[7:]
        #print(row_code,place_code)


        start_row = 0
        stop_row  = 127

        start_plc = 0
        stop_plc = 7

        #the fast way
        #test = row_code.replace("F","0").replace("B","1")
        #print(test,int(test,2))

        #ok now iterate the code...
        #the fun way
        row=iterate_code(row_code,0,127,"F","B")
        place=iterate_code(place_code,0,7,"L","R")

        id =row*8+place
        print(seat_code, row,place,id)

        id_list.append(id)

        if id > max_id:
            max_id=id



    print("MAX ID:",max_id)


def run():
    global input
    print("s1")
    input=remove_spaces( get_input("real_input.input"))
    check_rows()


