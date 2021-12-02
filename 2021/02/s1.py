from helper.helpers import  *

input=""




def run():
    global input
    print("s1")
    input=line_to_words(  get_input("real_input.input") )
    print(input)

    x_pos=0
    y_pos=0

    for line in input:
        if line[0] == "forward":
            x_pos += int(line[1].strip())
        elif line[0] == "up":
            y_pos -= int(line[1].strip())
        elif line[0] == "down":
            y_pos += int(line[1].strip())

        #print(x_pos,y_pos)
    print(x_pos,y_pos)
    print(x_pos*y_pos)


