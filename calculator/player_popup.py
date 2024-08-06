# player_popup.py
import tkinter as tk
from classes import Player

def add_new_player(root, players):
    def submit_player_info():
        name = entry_name.get()
        handicap = combobox_handicap.get()
        
        try:
            # handicap are chosen from
            # 0 (default)
            # .25
            # .5
            # .75
            # 1
            new_player = Player(root, players, name=name, handicap=handicap)
            players.append(new_player)
            new_player.add_score_entry(root)  # Optionally add a score entry for the new player
            popup.destroy()
        except ValueError:
            label_error.config(text="Please enter valid numbers for rounds and handicap.")
    
    pad_x = 5
    pad_y = 10

    popup = tk.Toplevel(root)
    popup.title("Add New Player")
    
    ### INPUTS

    # NAME 
    label_name = tk.Label(popup, text="Name:")
    label_name.grid(row=0, column=0, padx=pad_x, pady=pad_y)
    entry_name = tk.Entry(popup)
    entry_name.grid(row=0, column=1, padx=pad_x, pady=pad_y)
    
    # HANDICAP
    label_handicap = tk.Label(popup, text="Handicap:")
    label_handicap.grid(row=1, column=0, padx=pad_x, pady=pad_y)
    handicap_options = ["0", ".25", ".5", ".75", "1"]
    handicap_var = tk.StringVar()
    combobox_handicap = tk.Combobox(popup, textvariable=handicap_var, values=handicap_options, state="readonly")
    combobox_handicap.grid(row=1, column=1, padx=pad_x, pady=pad_y)
    combobox_handicap.current(0)  # Set the default value to "0"
    
    # SUBMIT BUTTON
    button_submit = tk.Button(popup, text="Submit", command=submit_player_info)
    button_submit.grid(row=3, column=0, columnspan=2, padx=pad_x, pady=pad_y)
    
    # error
    label_error = tk.Label(popup, text="", fg="red")
    label_error.grid(row=4, column=0, columnspan=2, padx=pad_x, pady=pad_y)
