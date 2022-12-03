from helper.helpers import  *

input=""


def run():
    global input
    print("\n\ns2")

    plays = Input(True).get()
    
    score_mapping = {
        "R": 1,
        "P": 2,
        "S": 3
    }
    
    mappings ={
        "A": "R",
        "B": "P",
        "C": "S",

        "X": "R",
        "Y": "P",
        "Z": "S"
    }

    lose = {
        "R": "P",
        "P": "S",
        "S": "R",
    }

    win ={
        "R": "S",
        "P": "R",
        "S": "P"
    }

    all_score = 0

    for game in plays:
        print("\nRound start:")
        
        inputs =  game.split(" ")
        print(f"  Round input: {inputs}")
        base_score = 0
        win_score = 0

        match inputs[1]:
            case "X":
                print("   lose round")
                win_score = 0
                
                base_score = score_mapping[ win[ mappings[ inputs[0]] ]]
            case "Y":
                print("   draw round")
                win_score = 3
                base_score = score_mapping[ mappings[inputs[0]]]
            case "Z":
                print("   win round")
                win_score = 6
                base_score = score_mapping[ lose[ mappings[ inputs[0]] ]]

        print(f"  Round base:  {base_score}")
        print(f"  Round state: {win_score}")
        
        all_score+= base_score + win_score

    print(f"All score: {all_score}")