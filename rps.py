import tkinter as tk
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!", 1, 0
    else:
        return "You lose!", 0, 1

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result, user_points, computer_points = determine_winner(user_choice, computer_choice)
    user_score += user_points
    computer_score += computer_points
    display_result(user_choice, computer_choice, result)

def display_result(user_choice, computer_choice, result):
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}\nUser Score: {user_score} | Computer Score: {computer_score}")

# Initialize scores
user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Buttons
rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.grid(row=0, column=2, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
