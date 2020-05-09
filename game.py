
REV_CLASS_MAP = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "none"
}

#  0_Rock  1_Paper  2_Scissors  

def mapper(val):
    return REV_CLASS_MAP[val]

def calculate_winner(move1, move2):
    if move1 == move2:
        return "Tie"

    if move1 == "rock":
        if move2 == 2:
            return "User"
        if move2 == 1:
            return "Computer"

    if move1 == "paper":
        if move2 == 0:
            return "User"
        if move2 == 2:
            return "Computer"

    if move1 == "scissors":
        if move2 == 2:
            return "User"
        if move2 == 0:
            return "Computer"