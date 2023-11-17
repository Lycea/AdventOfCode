from helper.helpers import  *

input=""



def parse():
    global input
    input = Input(False).get()
    
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

    most_seeable = 0

    for row_idx, row in enumerate(input):
        print("\n",row)
        for tree_idx, tree_height in enumerate(row):
            print(tree_idx, tree_height)

            column = [ input[x][tree_idx] for x in range(len(input)) ]
            #print(column)
            directions =[
                list(reversed( row[0:max(tree_idx,0)])),
                row[tree_idx+1:],
                list(reversed(column[0:max(row_idx,0)])),
                column[row_idx+1:]
                ]
            
            #print(directions)

            tree_seeable = 0
            for dir_idx, direction in enumerate(directions):
                dir_seeable = 0
                for other_tree in direction:
                    if other_tree >= tree_height:
                        break
                    dir_seeable+=1
                if len(direction)== 0 :
                    continue
                else:
                    if tree_seeable== 0:
                        tree_seeable = max(dir_seeable,1)
                    else:
                        tree_seeable*=max(dir_seeable,1)
                print( f"  {max(dir_seeable,1)}")
            print(tree_seeable)
            if tree_seeable > most_seeable:
                most_seeable = tree_seeable
    print(most_seeable)
def run():  
    print("\n\ns2")
    do()

    


