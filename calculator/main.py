# main.py
import tkinter as tk
from classes import Player, ScoreEntry
from player_popup import add_new_player

### GLOBAL VARIABLE
app_width = 640
app_height = 320

### WINDOWS HANDLING
# Function to center the window
def center_window(root):
    global app_width, app_height  # Declare global variables within this function
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position x and y coordinates
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    # Set the geometry of the window
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

# Create the main window
root = tk.Tk()
root.title("Shooting Competition Calculator")

# Center the window
center_window(root)

# Function to perform the calculation
def calculate():
    for player in players:
       player.calculate_total_score(player.scores)

players = []

# Button to calculate total score
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Button to add a new player
button_add_player = tk.Button(root, text="Add New Player", command=lambda: add_new_player(root, players))
button_add_player.grid(row=0, column=0, padx=10, pady=10)

# Run the application
root.mainloop()
