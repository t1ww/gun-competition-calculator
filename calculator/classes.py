# classes.py
import tkinter as tk

class Player:
    def __init__(self, root, players, name, handicap):
        self.name = name
        self.handicap = handicap
        self.score = 0
        self.scores = []
        self.row = len(players) + 1
        # name label
        self.label_name = tk.Label(root, text=self.name)
        self.label_name.grid(row=self.row, column=0, columnspan=1, padx=5, pady=10)

        # Label to display total score
        self.label_total_score = tk.Label(root, text=f"{self.score}")
        self.label_total_score.grid(row=self.row, column=len(self.scores)+1, padx=5, pady=10)

        # set first 2 score entries to be 5 rounds (default)

    def calculate_total_score(self, scores):
        total_score = 0
        try:    
            for score in scores:
                score_value = score.entry.get()
                if score_value.strip():  # Check if the entry is not empty after stripping whitespace
                    if(float(score_value) <= 0):
                        # calculate by deduction
                        total_score += ((score.rounds * 10) + float(score_value)) + self.handicap
                    else:
                        # calculate by sum
                        total_score += float(score_value) + self.handicap 
            self.score = total_score 
            self.label_total_score.config(text=f"{self.score}")
            return self.score
        except ValueError:
            return "Please enter valid numbers"

    
    def add_score_entry(self, root):
       index = len(self.scores)  # Calculate the index for the new ScoreEntry
       this_round = 2
       if index < 2 :
           this_round = 5
       new_score_entry = ScoreEntry(root, self.row, (index * 2) + 1, this_round, self.update_scores)
       self.scores.append(new_score_entry)
       self.label_total_score.grid(column=((index*2) + 4)) # move the total label

    def remove_score_entry(self):
        if self.scores:
            # Remove the last ScoreEntry from the grid
            last_score = self.scores.pop()
            last_score.entry.grid_forget()
            last_score.label.grid_forget()
            # Update the total score display position
            self.label_total_score.grid(column=(len(self.scores) * 2 + 4))
            self.update_scores()

    def update_scores(self, event=None):
        self.calculate_total_score(self.scores)

class ScoreEntry:
    def __init__(self, root, row, column, rounds, callback):
        # max score = rounds * 10
        self.rounds = rounds
        self.label = tk.Label(root, text=f"/{self.rounds}")
        self.label.grid(row=row, column=column+1, padx=5, pady=10)
        self.entry = tk.Entry(root, width=5)
        self.entry.grid(row=row, column=column+2, padx=1, pady=10)
        self.entry.bind('<KeyRelease>', callback)
