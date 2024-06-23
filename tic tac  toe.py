
def ttt(board): 
    for row in board: 
        print(" | ".join(row)) 
        print("__" * 5) 
 
def check(board, player): 
    
    for row in board: 
        if all([cell == player for cell in row]): 
            return True 
     
    for col in range(3): 
        if all([board[row][col] == player for row in range(3)]): 
            return True 
     
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]): 
        return True 
    return False 
 
def check_draw(board): 
    return all([cell != " " for row in board for cell in row]) 
 
def tic_tac_toe(): 
    board = [[" " for _ in range(3)] for _ in range(3)] 
    current_player = "#" 
 
    while True: 
        ttt(board) 
        row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): ")) 
        col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): ")) 
 
        if board[row][col] == " ": 
            board[row][col] = current_player 
        else: 
            print("Cell already taken, try again.") 
            continue 
 
        if check(board, current_player): 
            ttt(board) 
            print(f"Player {current_player} wins!") 
            break 
 
        if check_draw(board): 
            ttt(board) 
            print("It's a draw!") 
            break 
 
        current_player = "O" if current_player == "X" else "X" 
 
if __name__ == "__main__": 
    tic_tac_toe()


import random 
 
def roll_dice(): 
    return random.randint(1, 6) 
 
def move_player(player, steps): 
    player += steps 
    if player > 100: 
        player = 100 - (player - 100)  
    return player 
 
def check_snake_or_ladder(position): 
    snakes_and_ladders = { 
        4: 14, 9: 31, 17: 7, 20: 38, 28: 84, 40: 59, 
        51: 67, 54: 34, 62: 19, 63: 81, 64: 60, 71: 91, 
        87: 24, 93: 73, 95: 75, 99: 78 
    } 
    return snakes_and_ladders.get(position, position) 
 
def main(): 
    player_position = 0 
 
    while player_position < 100: 
        input("Press Enter to roll the dice") 
        steps = roll_dice() 
        print("You rolled a", steps) 
        player_position = move_player(player_position, steps) 
        player_position = check_snake_or_ladder(player_position) 
        print("You are now at position", player_position) 
 
    print("Congratulations You won!") 
 
if __name__ == "__main__": 
    main()