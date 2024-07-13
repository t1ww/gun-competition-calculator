import tkinter as tk

### GLOBAL VARIABLE
app_width = 360
app_height = 220

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

### SCORES HANDLING
# player class
class Player:
    def __init__(self, name, rounds, handicap):
        self.name = name
        self.rounds = rounds
        self.handicap = handicap
        self.score = 0
        self.scores = []
        self.row = len(players)
        # name label
        self.label_name = tk.Label(root, text=self.name)
        self.label_name.grid(row=self.row, column=0, columnspan=2, padx=10, pady=10)

        # Button to add a new ScoreEntry
        self.button_add_score = tk.Button(root, text="Add Score Entry", command=self.add_score_entry)
        self.button_add_score.grid(row=self.row, column=0, columnspan=2, padx=10, pady=10)
        # Label to display total score
        self.label_total_score = tk.Label(root, text=f"{self.score}")
        self.label_total_score.grid(row=self.row, column=len(self.scores)+1, padx=5, pady=10)

    def calculate_total_score(self, scores):
        try:
            self.score = sum(float(score.entry.get()) for score in scores)
            self.label_total_score.config(text=f"{self.score}")
            return self.score
        except ValueError:
            return "Please enter valid numbers"
    
    def add_score_entry(self):
       global app_height
       index = len(self.scores)  # Calculate the index for the new ScoreEntry
       new_score_entry = ScoreEntry(root, self.row, index + 1)  # Place new entry next to existing ones
       self.scores.append(new_score_entry)
       self.label_total_score.grid(column=index+3) # move the total label

# entry class
class ScoreEntry:
    def __init__(self, root, row, column):
        self.entry = tk.Entry(root, width=5)
        self.entry.grid(row=row, column=column+1, padx=5, pady=10)

# Function to perform the calculation
def calculate():
    for player in players:
       player.calculate_total_score(player.scores)
       

players = []
# Create a player
players.append(Player(name="urmom",rounds=10, handicap=5))
players.append(Player(name="nigga",rounds=10, handicap=5))

# Create ScoreEntries
players[0].add_score_entry()
players[1].add_score_entry()

# Button to calculate total score
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
