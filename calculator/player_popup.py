# player_popup.py
import tkinter as tk
from classes import Player

def add_new_player(root, players):
    def submit_player_info():
        name = entry_name.get()
        rounds = entry_rounds.get()
        handicap = entry_handicap.get()
        
        try:
            rounds = int(rounds)
            handicap = int(handicap)
            new_player = Player(root, players, name=name, rounds=rounds, handicap=handicap)
            players.append(new_player)
            new_player.add_score_entry(root)  # Optionally add a score entry for the new player
            popup.destroy()
        except ValueError:
            label_error.config(text="Please enter valid numbers for rounds and handicap.")
    
    popup = tk.Toplevel(root)
    popup.title("Add New Player")
    
    label_name = tk.Label(popup, text="Name:")
    label_name.grid(row=0, column=0, padx=10, pady=10)
    entry_name = tk.Entry(popup)
    entry_name.grid(row=0, column=1, padx=10, pady=10)
    
    label_rounds = tk.Label(popup, text="Rounds:")
    label_rounds.grid(row=1, column=0, padx=10, pady=10)
    entry_rounds = tk.Entry(popup)
    entry_rounds.grid(row=1, column=1, padx=10, pady=10)
    
    label_handicap = tk.Label(popup, text="Handicap:")
    label_handicap.grid(row=2, column=0, padx=10, pady=10)
    entry_handicap = tk.Entry(popup)
    entry_handicap.grid(row=2, column=1, padx=10, pady=10)
    
    button_submit = tk.Button(popup, text="Submit", command=submit_player_info)
    button_submit.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    label_error = tk.Label(popup, text="", fg="red")
    label_error.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
