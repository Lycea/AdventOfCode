from helper.helpers import  *

input=""

def check_yes():
    yes_answers = 0
    for group in input:
        answers = {}
        for person in group:
            for letter in person:
                #print(letter)
                if letter in answers:
                    answers[letter]+=1
                else:
                    answers[letter]=1

        #part two addition
        for answer in answers:
            if answers[answer]== len(group):
                yes_answers+=1

    print(yes_answers)


def run():
    global input
    print("s2")
    input= parse_by_next_new_line_array( get_input("real_input.input"))

    check_yes()


