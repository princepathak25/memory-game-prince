# 🃏 Emoji Memory Match Game by Prince Pathak
# A beautiful and fun Tkinter GUI game to test your memory with emoji cards!

import random
import tkinter as tk
from tkinter import messagebox

# 🧠 Emoji pairs
EMOJIS = ['🐶', '🐱', '🐻', '🦊', '🐸', '🐼', '🐵', '🦁']
PAIRS = EMOJIS * 2
random.shuffle(PAIRS)

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🃏 Memory Match Game by Prince")
        self.root.config(bg="#1e1e1e")
        self.buttons = []
        self.first_card = None
        self.second_card = None
        self.matched = 0

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="🧠 Match the Emoji Pairs!", font=("Segoe UI", 18), bg="#1e1e1e", fg="white")
        title.pack(pady=10)

        frame = tk.Frame(self.root, bg="#1e1e1e")
        frame.pack()

        for i in range(4):
            for j in range(4):
                btn = tk.Button(
                    frame, text="❓", width=6, height=3,
                    font=("Segoe UI", 20), bg="#444", fg="white",
                    command=lambda idx=(i * 4 + j): self.reveal_card(idx)
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(btn)

    def reveal_card(self, index):
        if self.buttons[index]["text"] != "❓":
            return

        self.buttons[index]["text"] = PAIRS[index]
        self.buttons[index].update()

        if self.first_card is None:
            self.first_card = index
        elif self.second_card is None and index != self.first_card:
            self.second_card = index
            self.root.after(700, self.check_match)

    def check_match(self):
        if PAIRS[self.first_card] == PAIRS[self.second_card]:
            self.buttons[self.first_card]["bg"] = "#33cc33"
            self.buttons[self.second_card]["bg"] = "#33cc33"
            self.matched += 1
        else:
            self.buttons[self.first_card]["text"] = "❓"
            self.buttons[self.second_card]["text"] = "❓"

        self.first_card = None
        self.second_card = None

        if self.matched == len(EMOJIS):
            messagebox.showinfo("🎉 Winner!", "You've matched all pairs!")
            self.root.after(1000, self.root.destroy)

# 🖥️ Launch GUI
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
# 🏁 End of the game