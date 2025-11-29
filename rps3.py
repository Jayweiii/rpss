import tkinter as tk
import random

options = ["rock", "paper", "scissors"]


def play(user_choice):
    computer_choice = random.choice(options)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")


# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x250")
root.resizable(False, False)

label = tk.Label(root, text="Choose:", font=("Arial", 14))
label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10,
                      command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10,
                       command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10,
                          command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
