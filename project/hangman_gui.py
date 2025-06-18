import tkinter as tk
from tkinter import messagebox
import random

# Setup
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x400")

# Game Data
words = ["python", "apple", "robot", "laptop", "music"]
secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6

# UI Variables
word_display = tk.StringVar()
attempts_display = tk.StringVar(value=f"Attempts Left: {attempts_left}")

# Functions
def display_word():
    return ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])

def check_guess():
    global attempts_left

    guess = entry_guess.get().lower()
    entry_guess.delete(0, tk.END)

    if not guess or len(guess) != 1 or not guess.isalpha():
        messagebox.showinfo("Invalid", "Please enter a single letter.")
        return

    if guess in guessed_letters:
        messagebox.showinfo("Already guessed", "You already guessed that letter.")
        return

    guessed_letters.append(guess)

    if guess in secret_word:
        word_display.set(display_word())
        if all(letter in guessed_letters for letter in secret_word):
            messagebox.showinfo("Congratulations", f"You guessed the word: {secret_word}")
            root.quit()
    else:
        attempts_left -= 1
        attempts_display.set(f"Attempts Left: {attempts_left}")
        if attempts_left == 0:
            messagebox.showinfo("Game Over", f"The word was: {secret_word}")
            root.quit()

# Widgets
label_word = tk.Label(root, textvariable=word_display, font=('Arial', 20))
label_word.pack(pady=10)

label_attempts = tk.Label(root, textvariable=attempts_display)
label_attempts.pack()

entry_guess = tk.Entry(root)
entry_guess.pack()

submit_button = tk.Button(root, text="Guess", command=check_guess)
submit_button.pack(pady=10)

# Initialize display
word_display.set(display_word())

# Start GUI
root.mainloop()
