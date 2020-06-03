MOVES = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "none"
}

#  0_Rock  1_Paper  2_Scissors


def find_winner(move1, move2):

    if move1 == "rock":
        if move2 == "scissors":
            return 1
        if move2 == "paper":
            return 0

    if move1 == "paper":
        if move2 == "rock":
            return 1
        if move2 == "scissors":
            return 0

    if move1 == "scissors":
        if move2 == "paper":
            return 1
        if move2 == "rock":
            return 0

    return "Tie"


def move_conv(val):
    return MOVES[val]
