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
        self.label_name.grid(row=self.row, column=0, columnspan=2, padx=10, pady=10)

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
                    total_score += float(score_value) # + handicap !!!
            self.score = self.max_score + total_score 
            self.label_total_score.config(text=f"{self.score}")
            return self.score
        except ValueError:
            return "Please enter valid numbers"

    
    def add_score_entry(self, root):
       index = len(self.scores)  # Calculate the index for the new ScoreEntry
       new_score_entry = ScoreEntry(root, self.row, index + 1, self.update_scores)
       self.scores.append(new_score_entry)
       self.label_total_score.grid(column=index+3) # move the total label

    def update_scores(self, event=None):
        self.calculate_total_score(self.scores)

class ScoreEntry:
    def __init__(self, root, row, column, callback):
        # max score = rounds * 10
        self.entry = tk.Entry(root, width=5)
        self.entry.grid(row=row, column=column+1, padx=5, pady=10)
        self.entry.bind('<KeyRelease>', callback)
