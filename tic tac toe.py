# Import the tkinter library for GUI creation and messagebox for displaying alert dialogs
import tkinter as tk
from tkinter import messagebox

# Function to check if there is a winner
def check_winner():
    # Define all possible winning combinations in a Tic-Tac-Toe game
    for combo in[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        # Check if all three buttons in a combo have the same non-empty text
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            # Highlight the winning buttons in green
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            # Show a messagebox announcing the winner
            messagebox.showinfo("Tic-Tac-Toe", f"player {buttons[combo[0]]['text']} wins!")
             # Exit the game after a winner is declared
            root.quit()

# Function to handle button clicks
def button_click(index):
    # Ensure the clicked button is empty and the game is not already won
    if buttons[index]["text"] == "" and not winner:
        # Set the button's text to the current player's symbol
        buttons[index]["text"] = current_player
        # Check if the current player has won
        check_winner()
        # Switch to the other player
        toggle_player()

# Function to toggle the current player
def toggle_player():
    global current_player
    # Switch between "X" and "O"
    current_player = "X" if current_player == "O" else "O"
    # Update the label to show whose turn it is
    label.config(text=f"player {current_player}'s turn")

# Create the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")  # Set the title of the window

# Create a list of 9 buttons for the Tic-Tac-Toe grid
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i))for i in range(9)]

 # Arrange the buttons in a 3x3 grid   
for i, button in enumerate(buttons):
    button.grid(row=i //3, column=i % 3)

# Initialize the current player to "X"
current_player = "X"
# Boolean to indicate if there's a winner (not used effectively in current code)
winner = False
# Create a label to display the current player's turn
label = tk.Label(root, text= f"player{current_player}'s turn", font=("normal",16))
label.grid(row=3, column=0, columnspan=3) # Place the label below the grid, spanning all columns

# Start the main event loop of the application
root.mainloop()
