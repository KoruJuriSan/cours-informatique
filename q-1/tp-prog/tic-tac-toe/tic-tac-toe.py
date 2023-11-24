def correct_tic_tac_toe_user_enties(entry):
    result = {"y": None, "x": None}
    if (len(entry) != 2): return False

    if (entry[0] in ["a", "b", "c"]):
        result["y"] = entry[0]

    if (entry[1] in ["a", "b", "c"]):
        result["y"] = entry[1]

    if (entry[0] in ["1", "2", "3"]):
        result["x"] = int(entry[0])

    if (entry[1] in ["1", "2", "3"]):
        result["x"] = int(entry[1])
    
    if (result["y"] != None and result["x"] != None): return result
    return False

def inverse_player_turn(player_turn):
    if player_turn == "x": return "o"
    if player_turn == "o": return "x"

def tic_tac_toe_turn(current_board: dict, player_turn: str, move: dict):
    new_board = current_board
    if new_board[move["y"]][move["x"]] == None: new_board[move["y"]][move["x"]] = player_turn.upper()
    else: return [current_board, player_turn, True]

    for y, yValues in new_board.items():
        if (yValues[1] == yValues[2] == yValues[3] and yValues[1] in ["X", "Y"]): return [current_board, player_turn, False]
    
    for i in range(1, 4):
        if (new_board["a"][i] == new_board["b"][i] == new_board["c"][i] and new_board["a"][i] in ["X", "Y"]): return [current_board, player_turn, False]

    if (new_board["a"][1] == new_board["b"][2] == new_board["c"][3] and new_board["a"][1] in ["X", "Y"]): return [current_board, player_turn, False]
    if (new_board["a"][3] == new_board["b"][2] == new_board["c"][1] and new_board["a"][3] in ["X", "Y"]): return [current_board, player_turn, False]

    return [new_board, inverse_player_turn(player_turn), True]

def show_board(board):
    board_GUI = "| / | 1 | 2 | 3 |\n"
    size_x = 3
    size_y = "c"

    for y, yValues in board.items():
        board_GUI += f"| {y} |"
        for x, value in yValues.items():
            if (value == None):
                board_GUI += f" - |"
            else:
                board_GUI += f" {value} |"
        if (y != size_y): board_GUI += "\n"

    print(board_GUI)


def tic_tac_toe():
    player_turn: str = "x"
    choice = False
    board: dict = {
        'a': {1: None, 2: None, 3: None},
        'b': {1: None, 2: None, 3: None},
        'c': {1: None, 2: None, 3: None},
    }
    game_in_progress = True
    while game_in_progress:
        show_board(board)
        print(f"It's {player_turn}'s turn, choose where you want to put your {player_turn.upper()}")
        while choice == False:
            choice = correct_tic_tac_toe_user_enties(input("Position (ex: b3): "))
        [board, player_turn, game_in_progress] = tic_tac_toe_turn(board, player_turn, move=choice)
        choice = False
    show_board(board)
    print(f"The winner is {player_turn}")

def main():
    tic_tac_toe()


if __name__ == "__main__":
    main()