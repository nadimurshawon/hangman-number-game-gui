import tkinter as tk
import random


stages = [
    """
       +---+
           |
           |
           |
          ===""",
    """
       +---+
       O   |
           |
           |
          ===""",
    """
       +---+
       O   |
       |   |
           |
          ===""",
    """
       +---+
       O   |
      /|   |
           |
          ===""",
    """
       +---+
       O   |
      /|\\  |
           |
          ===""",
    """
       +---+
       O   |
      /|\\  |
      /    |
          ===""",
    """
       +---+
       O   |
      /|\\  |
      / \\  |
          ==="""
]


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Number Guessing Game")

        self.wrong_guesses = 0
        self.max_attempts = 5
        self.random_number = random.randint(1, 10)

        self.label = tk.Label(root, text="Guess a number (1 to 100):")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Guess", command=self.check_guess)
        self.button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.hangman_display = tk.Label(root, text=stages[0], font=("Courier", 12))
        self.hangman_display.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid number!")
            return

        if guess == self.random_number:
            self.result_label.config(text="✅ Correct! You saved the man!")
            self.button.config(state="disabled")
        else:
            self.wrong_guesses += 1
            self.hangman_display.config(text=stages[self.wrong_guesses])
            self.result_label.config(text=f"❌ Wrong! The number was: {self.random_number}")
            if self.wrong_guesses >= self.max_attempts:
                self.result_label.config(text="💀 Game over. The man is hanged.")
                self.button.config(state="disabled")
            else:
                self.random_number = random.randint(1, 10)  

        self.entry.delete(0, tk.END)


root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
