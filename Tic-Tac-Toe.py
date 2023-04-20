import numpy as np
import tkinter as tk
import random

# Define the game board and player symbols
board = np.zeros((3,3))
player = 1
symbols = [' ', '❌', '⭕']

# Define colors for buttons
button_colors = ['#ffffff', '#ffcccc', '#ccccff']

# Define the GUI window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create a label to display the winner
winner_label = tk.Label(root, text="", font=('Helvetica', 18))

# Create a button for each cell on the board
buttons = [[tk.Button(root, text="", font=('Helvetica', 40), width=6, height=3, bg=button_colors[0], activebackground=button_colors[1], command=lambda row=i, col=j: button_click(row, col)) for j in range(3)] for i in range(3)]

# Place the buttons on the grid
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

# Define the functions to handle button clicks and check for a winner
def button_click(row, col):
    global player
    if board[row][col] == 0:
        board[row][col] = player
        buttons[row][col].config(text=symbols[player], state=tk.DISABLED, disabledforeground="black", bg=button_colors[player], activebackground=button_colors[player])
        check_for_winner()
        player = 2 if player == 1 else 1
        if player == 2:
            computer_play()

def check_for_winner():
    for player in [1, 2]:
        if (board[0] == [player, player, player]).all() or (board[1] == [player, player, player]).all() or (board[2] == [player, player, player]).all() or (board[:,0] == [player, player, player]).all() or (board[:,1] == [player, player, player]).all() or (board[:,2] == [player, player, player]).all() or (board[0,0] == player and board[1,1] == player and board[2,2] == player) or (board[0,2] == player and board[1,1] == player and board[2,0] == player):
            winner_label.config(text=f"{symbols[player]} wins! 🎉", fg=button_colors[player])
            disable_buttons()

    if np.all(board != 0):
        winner_label.config(text="It's a tie! 🤝",fg="#000000")
        disable_buttons()

def disable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=tk.DISABLED)

def computer_play():
    available_cells = np.argwhere(board == 0)
    if len(available_cells) > 0:
        row, col = random.choice(available_cells)
        button_click(row, col)

# Add the winner label to the window
winner_label.grid(row=3, column=0, columnspan=3)

# Run the GUI
root.mainloop()
