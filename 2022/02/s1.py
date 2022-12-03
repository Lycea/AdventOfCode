from helper.helpers import  *

input=""


def do():
    pass


def run():
    global input
    print("\n\ns1")
    plays = Input().get()
    
    score_mapping = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    
    mappings ={
        "A": "R",
        "B": "P",
        "C": "S",

        "X": "R",
        "Y": "P",
        "Z": "S"
    }

    all_score = 0

    for game in plays:
        print("\nRound start:")
        
        inputs =  game.split(" ")
        print(f"  Round input: {inputs}")
        base_score = score_mapping[inputs[1]]
        win_score = 0

        if mappings[inputs[1]] == mappings[inputs[0]] :
            win_score = 3
        elif mappings[inputs[1]] == "R" and mappings[inputs[0]] == "S":
            win_score = 6
        elif mappings[inputs[1]] == "P" and mappings[inputs[0]] == "R":
            win_score = 6
        elif mappings[inputs[1]] == "S" and mappings[inputs[0]] == "P":
            win_score = 6

        print(f"  Round base:  {base_score}")
        print(f"  Round state: {win_score}")
        
        all_score+= base_score + win_score

    print(f"All score: {all_score}")
    
        




