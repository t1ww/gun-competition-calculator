import tkinter as tk
from classes import Player
from player_popup import add_new_player

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

# Initialize the list of players
players = []

# Function to add score entries
def add_score_entries():
    for player in players:
        player.add_score_entry(root)

# Create the button to add score entries
button_add_score_entries = tk.Button(root, text="Add Score Entries", command=add_score_entries)
button_add_score_entries.grid(row=0, column=1, padx=10, pady=10)

# Create the button to add a new player
button_add_player = tk.Button(root, text="Add Player", command=lambda: add_new_player(root, players, max_score, rounds))
button_add_player.grid(row=0, column=0, padx=10, pady=10)

# Button to calculate total score
button_calculate = tk.Button(root, text="Calculate", command=lambda: calculate(players))
button_calculate.grid(row=1, column=0, padx=10, pady=10)

# Function to perform the calculation
def calculate(players):
    for player in players:
       player.calculate_total_score(player.scores)

# Run the application
root.mainloop()
