
import tkinter as tk
import random

# -------------------- Data --------------------
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫"}

player_score = 0
computer_score = 0
round_no = 1

# -------------------- Logic --------------------
def check_winner(you, computer):
    if computer == you:
        return "🤝 It's a Draw"

    if computer == -1 and you == 1:
        return "✅ You Win!"
    elif computer == -1 and you == 0:
        return "❌ You Lose!"
    elif computer == 1 and you == -1:
        return "❌ You Lose!"
    elif computer == 1 and you == 0:
        return "✅ You Win!"
    elif computer == 0 and you == -1:
        return "✅ You Win!"
    elif computer == 0 and you == 1:
        return "❌ You Lose!"
    else:
        return "⚠ Something went wrong"


def play(youstr):
    global player_score, computer_score, round_no

    you = youDict[youstr]
    computer = random.choice([-1, 0, 1])

    result = check_winner(you, computer)

    # Update scores
    if "Win" in result:
        player_score += 1
    elif "Lose" in result:
        computer_score += 1

    # Update UI
    player_label.config(text=f"You Chose: {reverseDict[you]}")
    computer_label.config(text=f"Computer Chose: {reverseDict[computer]}")
    result_label.config(text=f"Result: {result}")

    score_label.config(
        text=f"You: {player_score}   Computer: {computer_score}   Round: {round_no}"
    )

    round_no += 1


# -------------------- GUI --------------------
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("1200x620")
root.resizable(True, True)

title = tk.Label(
    root,
    text="🎮 Snake  Water  Gun 🎮",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

player_label = tk.Label(root, text="You Chose: ", font=("Arial", 12))
player_label.pack()

computer_label = tk.Label(root, text="Computer Chose: ", font=("Arial", 12))
computer_label.pack()

result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=10)

score_label = tk.Label(
    root,
    text="You: 0   Computer: 0   Round: 1",
    font=("Arial", 12)
)
score_label.pack(pady=10)

# -------------------- Buttons --------------------
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

snake_btn = tk.Button(
    btn_frame,
    text="🐍 Snake",
    font=("Arial", 12),
    width=10,
    command=lambda: play("s")
)
snake_btn.grid(row=0, column=0, padx=5)

water_btn = tk.Button(
    btn_frame,
    text="💧 Water",
    font=("Arial", 12),
    width=10,
    command=lambda: play("w")
)
water_btn.grid(row=0, column=1, padx=5)

gun_btn = tk.Button(
    btn_frame,
    text="🔫 Gun",
    font=("Arial", 12),
    width=10,
    command=lambda: play("g")
)
gun_btn.grid(row=0, column=2, padx=5)

exit_btn = tk.Button(
    root,
    text="Exit",
    font=("Arial", 11),
    width=10,
    command=root.quit
)
exit_btn.pack(pady=15)

root.mainloop()
