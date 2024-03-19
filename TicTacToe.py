{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85d6d77f-e6f9-4ad6-93aa-30c1e085e341",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Define the game board\n",
    "board = np.full((3,3), ' ')\n",
    "\n",
    "# Function to display the board\n",
    "def display_board(board):\n",
    "    for row in board:\n",
    "        print('|'.join(row))\n",
    "        print('-'*5)\n",
    "\n",
    "# Display the initial board\n",
    "display_board(board)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7644f4f-a3bf-4bc8-bd36-ab016667b83d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import messagebox\n",
    "import numpy as np\n",
    "\n",
    "# Initialize the game board\n",
    "board = np.full((3,3), ' ')\n",
    "\n",
    "# Function to check for win or draw\n",
    "def check_win():\n",
    "    # Implement win check logic here\n",
    "    pass\n",
    "\n",
    "# Function to handle player move\n",
    "def player_move(row, col):\n",
    "    global board\n",
    "    if board[row][col] == ' ':\n",
    "        board[row][col] = 'X'\n",
    "        button_list[row][col].config(text='X')\n",
    "        check_win()\n",
    "        # Call AI move function here\n",
    "    else:\n",
    "        messagebox.showwarning(\"Invalid Move\", \"This cell is already taken!\")\n",
    "\n",
    "# Function to create the game board GUI\n",
    "def create_board_gui(window):\n",
    "    global button_list\n",
    "    button_list = [[None for _ in range(3)] for _ in range(3)]\n",
    "    for row in range(3):\n",
    "        for col in range(3):\n",
    "            button = tk.Button(window, text=' ', width=10, height=3,\n",
    "                               command=lambda r=row, c=col: player_move(r, c))\n",
    "            button.grid(row=row, column=col)\n",
    "            button_list[row][col] = button\n",
    "\n",
    "# Main function to run the game\n",
    "def run_game():\n",
    "    window = tk.Tk()\n",
    "    window.title(\"Tic-Tac-Toe AI\")\n",
    "    create_board_gui(window)\n",
    "    window.mainloop()\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    run_game()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
