import tkinter as tk
import random

# List of words
WORDS = ["python", "hangman", "developer", "software", "engineering"]

# Global Variables
attempts = 0  # Tracks wrong guesses (max 6)
word = random.choice(WORDS)  # Random word selection
guessed_word = ["_"] * len(word)
hangman_parts = []  # Stores body part functions

# Create Tkinter window
root = tk.Tk()
root.title("Hangman Game")

# Canvas for drawing
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.grid(row=0, column=0, columnspan=2)

# Labels and Inputs
label_word = tk.Label(root, text=" ".join(guessed_word), font=("Arial", 16))
label_word.grid(row=1, column=0, columnspan=2)

entry_letter = tk.Entry(root)
entry_letter.grid(row=2, column=0)

btn_guess = tk.Button(root, text="Guess")
btn_guess.grid(row=2, column=1)

label_message = tk.Label(root, text="", font=("Arial", 12))
label_message.grid(row=3, column=0, columnspan=2)

# Function to draw gallows
def draw_gallows():
    """Draw the initial gallows."""
    canvas.create_line(50, 250, 150, 250, width=3)  # Base
    canvas.create_line(100, 250, 100, 50, width=3)   # Pole
    canvas.create_line(100, 50, 200, 50, width=3)    # Top beam
    canvas.create_line(200, 50, 200, 80, width=3)    # Rope

# Functions to draw hangman body parts
def draw_head():
    canvas.create_oval(180, 80, 220, 120, width=3)

def draw_body():
    canvas.create_line(200, 120, 200, 180, width=3)

def draw_left_arm():
    canvas.create_line(200, 130, 170, 160, width=3)

def draw_right_arm():
    canvas.create_line(200, 130, 230, 160, width=3)

def draw_left_leg():
    canvas.create_line(200, 180, 170, 220, width=3)

def draw_right_leg():
    canvas.create_line(200, 180, 230, 220, width=3)

# Add drawing functions to a list
hangman_parts = [draw_head, draw_body, draw_left_arm, draw_right_arm, draw_left_leg, draw_right_leg]

# Function to handle guesses
def make_guess():
    global attempts
    letter = entry_letter.get().lower()
    entry_letter.delete(0, tk.END)

    if not letter or len(letter) > 1 or not letter.isalpha():
        label_message.config(text="Enter a single letter.", fg="red")
        return

    if letter in guessed_word:
        label_message.config(text="Already guessed this letter!", fg="orange")
        return

    if letter in word:
        # Reveal the guessed letter in the word
        for i, char in enumerate(word):
            if char == letter:
                guessed_word[i] = letter
        label_word.config(text=" ".join(guessed_word))

        # Check for win
        if "_" not in guessed_word:
            label_message.config(text="You win!", fg="green")
            btn_guess.config(state=tk.DISABLED)
    else:
        # Draw the next hangman part
        if attempts < len(hangman_parts):
            hangman_parts[attempts]()  # Draw next part
            attempts += 1

        if attempts >= len(hangman_parts):
            label_message.config(text=f"You lost! The word was '{word}'", fg="red")
            btn_guess.config(state=tk.DISABLED)

# Bind button to guess function
btn_guess.config(command=make_guess)

# Initialize game
draw_gallows()

# Run the Tkinter main loop
root.mainloop()