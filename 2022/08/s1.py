from helper.helpers import  *

input=""



def parse():
    global input
    input = Input(True).get()
    
def do():
    parse()

    visible_list ={}
    seeable_trees = 0

    seeable_trees += len(input[0])*2
    seeable_trees += (len(input)-2) * 2

    for num in range(len(input[0])):
        visible_list[f"{0}/{num}"] = True
        visible_list[f"{len(input)-1}/{num}"] = True
    for num in range(1,len(input)-1):
        visible_list[f"{num}/{0}"] = True
        visible_list[f"{num}/{len(input)-1}"] = True
    
    print(f"Base seeable: {seeable_trees}")

    

    for row_idx, row in enumerate(input):
        highest_tree = max(row)
        highest_prev = -1

        #forward
        for idx , num in enumerate(row):
            num = int(num)
            if num > highest_prev :
                highest_prev = num

                #if idx != 0 or idx != len(row)-1:
                #    seeable_trees+=1
                vis_idx = f"{row_idx}/{idx}"
                if vis_idx in visible_list:
                    pass
                else:
                    print(f"add {vis_idx}: {num}")
                    visible_list[vis_idx]=True
                    seeable_trees+=1
            if num == highest_tree:
                break
        
        highest_prev = -1
        #backward
        for idx , num in enumerate( reversed(row)):
            idx = len(row)-1 -idx
            num = int(num)
            print(num)
            if num > highest_prev :
                highest_prev = num

                #if idx != 0 or idx != len(row)-1:
                #    seeable_trees+=1
                vis_idx = f"{row_idx}/{idx}"
                if vis_idx in visible_list:
                    pass
                else:
                    print(f"add {vis_idx}: {num} (rev)")
                    visible_list[vis_idx]=True
                    seeable_trees+=1
            if num == highest_tree:
                break

    for col_idx in range(len(input[0])):
        highest_tree = max( [ input[x][col_idx] for x in range(len(input)) ]      )
        highest_prev = -1

        #print("h",highest_tree)
        #forward
        for idx in range(len(input)):
            num = int( input[idx][col_idx])
            if num > highest_prev :
                highest_prev = num

                #if idx != 0 or idx != len(row)-1:
                #    seeable_trees+=1
                vis_idx = f"{idx}/{col_idx}"
                if vis_idx in visible_list:
                    pass
                else:
                    print(f"add {vis_idx}: {num}")
                    visible_list[vis_idx]=True
                    seeable_trees+=1
            if num == highest_tree:
                break
        
        highest_prev = -1
        #backward
        for idx  in range(len(input[0])-1,-1,-1):
            #print("rev_idx",idx)
            #idx = len(row)-1 -idx
            num = int(input[idx][col_idx])
            #print(num)
            if num > highest_prev :
                highest_prev = num

                #if idx != 0 or idx != len(row)-1:
                #    seeable_trees+=1
                vis_idx = f"{idx}/{col_idx}"
                if vis_idx in visible_list:
                    pass
                else:
                    print(f"add {vis_idx}: {num} (rev)")
                    visible_list[vis_idx]=True
                    seeable_trees+=1
            if num == highest_tree:
                break

    print(seeable_trees)

def run():  
    print("\n\ns1")
    do()

    


