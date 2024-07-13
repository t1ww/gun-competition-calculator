import tkinter as tk

### GLOBAL VARIABLE

app_width = 300
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
# players
class Player:
    def __init__(self, name, rounds, handicap):
        self.name = name
        self.rounds = rounds
        self.handicap = handicap
        self.score = 0

    def calculate_total_score(self, scores):
        try:
            self.score = sum(float(score.entry.get()) for score in scores)
            return self.score
        except ValueError:
            return "Please enter valid numbers"

# entries
class ScoreEntry:
    def __init__(self, root, label_text, row, column):
        self.label = tk.Label(root, text=label_text)
        self.label.grid(row=row, column=column, padx=10, pady=10)
        self.entry = tk.Entry(root)
        self.entry.grid(row=row, column=column+1, padx=10, pady=10)

# Function to add a new ScoreEntry
def add_score_entry():
    global app_height

    index = len(scores)  # Calculate the index for the new ScoreEntry
    new_score_entry = ScoreEntry(root, f"Score {index + 1}:", index + 2, 0)  # Place new entry below existing ones
    scores.append(new_score_entry)

    # Adjust the position of existing widgets
    button_add_score.grid(row=index + 3)  # Move the entry button down
    button_calculate.grid(row=index + 4)  # Move the calculate button down
    label_result.grid(row=index + 5)
    app_height += 42
    center_window(root)
    

# Function to perform the calculation
def calculate():
    total = player.calculate_total_score(scores)
    label_result.config(text=f"Total Score: {total}")

# Create initial ScoreEntry list
scores = []
scores.append(ScoreEntry(root, "Score 1:", 0, 0))
scores.append(ScoreEntry(root, "Score 2:", 1, 0))

# Create a player
player = Player(rounds=10, handicap=5)

# Button to add a new ScoreEntry
button_add_score = tk.Button(root, text="Add Score Entry", command=add_score_entry)
button_add_score.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Button to calculate total score
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Label to display total score
label_result = tk.Label(root, text="Total Score: ")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
