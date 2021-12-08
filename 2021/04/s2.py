from helper.helpers import  *
import math

input=""



boards =[]
pulls=[]

class Board:
    board_id = 1
    def __init__(self,raw_board):
        self.nums = {}
        self.rows = [ [] for x in range(5)  ]
        self.cols = [ [] for x in range(5)  ]

        self.id = Board.board_id
        Board.board_id+=1

        print(self.rows)

        numbers = list(filter(None,raw_board.split(" ")))

        for number_id in range(len(numbers)):
            row = math.floor( number_id /5)
            col = number_id%5

            self.nums[numbers[number_id]]={"r":row,"c":col}

            self.rows[row].append(numbers[number_id])
            self.cols[col].append(numbers[number_id])


        print(self.nums)
        print(self.rows)
        print(self.cols)

    def get_sum(self):
        sum= 0
        for num in self.nums.keys():
            sum+=int(num)

        return sum

    def check_bingo(self,number):
        print("  b "+str(self.id)+"  pulls "+number)
        if number in self.nums:
            #print("has number",number)

            row = self.nums[number]["r"]
            col = self.nums[number]["c"]

            self.rows[row].pop(self.rows[row].index(number))
            self.cols[col].pop(self.cols[col].index(number))

            self.nums.pop(number)

            if len(self.rows[row]) == 0 or len(self.cols[col]) == 0:
                return True
            else:
                return False

        return False

def run():
    global input

    global boards
    global pulls

    print("s2")
    input=get_input("real_input.input")

    chunks =parse_by_nex_new_line(input)

    pulls = chunks[0].split(",")
    print(pulls)

    for board in chunks[1:]:
        boards.append(Board(board))


    for pull in pulls:
        #print("number:",pull)
        for board_id in reversed(range(len(boards))):


            board = boards[board_id]

            if board.check_bingo(pull.strip()):
                board_sum = board.get_sum()

                print(board_sum,pull,board_sum*int(pull.strip()))
                print(board.id)

                boards.pop(boards.index(board))

            #if len(boards)==1:
            #    sum_ = boards[0].get_sum()
            #    print(sum_, pull, sum_ * int(pull.strip()))
            #    print(boards[0].id)
            #    exit()

