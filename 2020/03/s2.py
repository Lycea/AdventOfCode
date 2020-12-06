from helper.helpers import  *
import math
input=""


def replace_char(c,rep,idx):
    #print(c)
    c= c[:idx]+rep+c[idx+1:]
    #print(c)
    return c

def check_trees_in_path(x_walk_step,y_walk_step):
    x_walk_step = x_walk_step
    y_walk_step = y_walk_step

    map_height  = len(input)
    map_width   = len(input[0])

    found_trees = 0

    actual_line=0
    act_x      =0

    #print("Map height: ",map_height)
    #print("Map width:  ",map_width)

    #since we iterate all lines
    for line in range(0,map_height,y_walk_step):
        #print(line,actual_line)

        #print(line)
        line =input[line]
        #print("   Calc x",x_pos)

        #normalize it to the default line :P
        local_x =act_x%map_width   #math.floor( act_x/map_width)+

        #print(act_x%map_width)
       # print("local x ",local_x,line[local_x])
        #print(replace_char(line,"A",local_x))
        if line[local_x] =="#":
            #print("   found a tree...")
            found_trees+=1

        actual_line+=y_walk_step
        act_x+=x_walk_step


        #print(" "*10)

    print("FOUND TREES:",found_trees)
    return found_trees


def run():
    global input
    print("s2")
    input =list(filter(None,remove_spaces(get_input("real_input.input"))))
    print(input)
    slopes=[
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2]
    ]

    result = 0
    for slope in slopes:
        print(slope)
        res=check_trees_in_path(slope[0],slope[1])
        print(res)
        if result==0:
            result+=res
        else:
            result*=res
        print(result)
    print(result)


    print("-----------")

