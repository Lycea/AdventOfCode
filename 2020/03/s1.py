from helper.helpers import  *
import math
input=""


def replace_char(c,rep,idx):
    #print(c)
    c= c[:idx]+rep+c[idx+1:]
    #print(c)
    return c

def check_trees_in_path():
    x_walk_step = 3
    y_walk_step = 1

    map_height  = len(input)
    map_width   = len(input[0])

    found_trees = 0

    actual_line=0
    act_x      =0

    #print("Map height: ",map_height)
    #print("Map width:  ",map_width)

    #since we iterate all lines
    for line in input:
        print(line,actual_line)


        #print("   Calc x",x_pos)

        #normalize it to the default line :P
        local_x =act_x%map_width   #math.floor( act_x/map_width)+

        #print(act_x%map_width)
       # print("local x ",local_x,line[local_x])
        print(replace_char(line,"A",local_x))
        if line[local_x] =="#":
            print("   found a tree...")
            found_trees+=1

        actual_line+=y_walk_step
        act_x+=x_walk_step


        print(" "*10)

    print("FOUND TREES:",found_trees)


def run():
    global input
    print("s1")
    input =list(filter(None,remove_spaces(get_input("real_input.input"))))
    print(input)

    check_trees_in_path()
    print("-----------")

