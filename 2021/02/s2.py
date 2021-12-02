from helper.helpers import  *

input=""


def run():
    global input
    print("s2")

    input = line_to_words(get_input("real_input.input"))
    print(input)

    aim = 0

    x_pos = 0
    y_pos = 0

    for line in input:
        if line[0] == "forward":
            x_pos += int(line[1].strip())
            y_pos += aim*int(line[1].strip())
        elif line[0] == "up":
            aim -= int(line[1].strip())
        elif line[0] == "down":
            aim += int(line[1].strip())

        print(x_pos,y_pos)
    print(x_pos, y_pos)
    print(x_pos * y_pos)