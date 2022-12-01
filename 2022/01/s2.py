from helper.helpers import  *

input=""


def run():
    global input
    print("\ns2")
    
    input = get_input("input.input")
    elves = parse_by_next_new_line_array(input)
    
    all_list = []
    for elve in elves:
        calorie_list = lines_to_nums(elve)
        local_calories = sum(calorie_list)
        all_list.append(local_calories)
    
    print(f"Summed up: {sum(sorted(all_list)[-3:])}")