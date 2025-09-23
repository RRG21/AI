
"""
AI Practical-09.py
tic tac toe game
"""

import random
board = [" " for _ in range(9)]

def print_board() :
    for i in range(0,9,3):
        print(board[i] + "|" + board[i+1] + "|" + board[i+2])

def player_move():
    move = int(input("Choose your position (0-8): "))
    if board[move] == " ":
        board[move] = "X"

def ai_move():
    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)
    board[move] = "0"

while " " in board:
    print_board()
    player_move()
    if " " not in board:
        break
    ai_move()

print_board()
print("Game over")