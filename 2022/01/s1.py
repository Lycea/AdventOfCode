from helper.helpers import *
input=""




def run():
    global input
    print("\ns1")

    input = get_input("input.input")
    elves = parse_by_next_new_line_array(input)
    
    most_calories = 0
    for elve in elves:
        calorie_list = lines_to_nums(elve)
        local_calories = sum(calorie_list)
        if local_calories > most_calories:
            most_calories = local_calories
        
    print(f"Most callories are: {most_calories}")


