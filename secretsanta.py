import tkinter as tk
from tkinter import messagebox
import random

# Function to shuffle and assign Secret Santa
def assign_secret_santa():
    names = [entry.get() for entry in name_entries if entry.get().strip()]
    if len(names) < 2:
        messagebox.showerror("Error", "Please enter at least 2 names.")
        return

    participants = names[:]
    random.shuffle(participants)

    # Assign Secret Santa
    secret_santa_pairs = {}
    for i, name in enumerate(names):
        # Ensure no one gets their own name
        while participants[i] == name:
            random.shuffle(participants)
        secret_santa_pairs[name] = participants[i]

    # Display results
    results = "\n".join([f"{giver} -> {receiver}" for giver, receiver in secret_santa_pairs.items()])
    messagebox.showinfo("Secret Santa Assignments", results)

# Function to add more entry fields for participants
def add_name_entry():
    entry = tk.Entry(app, width=30)
    entry.pack(pady=2)
    name_entries.append(entry)

# GUI setup
app = tk.Tk()
app.title("Secret Santa Organizer")

# Title label
title_label = tk.Label(app, text="Secret Santa Organizer", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Instruction label
instruction_label = tk.Label(app, text="Enter the names of participants below:")
instruction_label.pack(pady=5)

# Name entry fields
name_entries = []
for _ in range(5):  # Start with 5 entry fields
    add_name_entry()

# Add name button
add_name_button = tk.Button(app, text="Add Another Name", command=add_name_entry)
add_name_button.pack(pady=5)

# Shuffle and assign button
assign_button = tk.Button(app, text="Assign Secret Santa", command=assign_secret_santa)
assign_button.pack(pady=10)

# Run the application
app.mainloop()
