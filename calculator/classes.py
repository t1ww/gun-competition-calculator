# classes.py
import tkinter as tk

class Player:
    def __init__(self, root, players, name, rounds, handicap):
        self.name = name
        self.rounds = rounds
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

    def calculate_total_score(self, scores):
        try:
            self.score = sum(float(score.entry.get()) for score in scores)
            self.label_total_score.config(text=f"{self.score}")
            return self.score
        except ValueError:
            return "Please enter valid numbers"
    
    def add_score_entry(self, root):
       index = len(self.scores)  # Calculate the index for the new ScoreEntry
       new_score_entry = ScoreEntry(root, self.row, index + 1)  # Place new entry next to existing ones
       self.scores.append(new_score_entry)
       self.label_total_score.grid(column=index+3) # move the total label

class ScoreEntry:
    def __init__(self, root, row, column):
        self.entry = tk.Entry(root, width=5)
        self.entry.grid(row=row, column=column+1, padx=5, pady=10)
