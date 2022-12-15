from helper.helpers import  *
import os

input=""
dir_sizes ={}

class cDir:
    def __init__(self,path,parent=None):
        self.path   = path
        self.files  = {}
        self.dirs   = {}
        self.parent = parent
        self.size   = 0

    def sum_size(self):
        for _ , dir in self.dirs.items():
            self.size += dir.sum_size()
        
        for file, size in self.files.items():
            self.size += size

        dir_sizes[self.path]=self.size
        #print(f"\nPath: {self.path}")
        #print(f"  Size: {self.size}")
        return self.size

    def add_file(self, name,size):
        self.files[name] = int(size)

    def add_dir(self, name):
        self.dirs[name] = cDir(os.path.join(self.path, name),self)
    
    def cd(self, direct_path):
        print("moving")
        match direct_path:
            case "/":
                return dir_tree
            case "..":
                return self.up()
            case _:
                return self.dirs[direct_path]
        

    def print(self,lvl=0):
        print(" "*(lvl*2)+f"| - {self.path}")
        for _, dir in self.dirs.items():
            dir.print(lvl+1)
        
        for file,_ in self.files.items():
            print(" "*((lvl+1)*2)+f"| - {file}:{_}")

    def up(self):
        return self.parent


dir_tree = cDir("/")

def parse():
    global input
    input=Input(True).get()
    
def do():
    parse()
    print(input)

    cur_dir = dir_tree
    #build
    for command in input:
        print(cur_dir.path)
        split_command = command.split(" ")
        #is a real command
        print(f"command:  {command}")
        if command.startswith("$"):
            print("  is command")
            if split_command[1] == "cd":
                print("   is cd")
                cur_dir = cur_dir.cd(split_command[2])
        else:
            print("  is listing")
            if split_command[0] == "dir":
                print("   is dir")
                cur_dir.add_dir(split_command[1])
            else:
                print("   is file")
                cur_dir.add_file(split_command[1],split_command[0])
    cur_dir = dir_tree
    dir_tree.print()
        
    dir_tree.sum_size()
    #build up tree

    total_filtered_size = 0

    for path,size in dir_sizes.items():
        if size < 100000:
            total_filtered_size+=size

    print(f"Filterable size: {total_filtered_size}")


def run():  
    print("\n\ns1")
    do()

    


