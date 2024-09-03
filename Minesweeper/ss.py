import tkinter as tk
from tkinter import simpledialog, messagebox

class Minesweeper:
    def __init__(self, master, rows, cols):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mine_grid = [[0]*cols for _ in range(rows)]
        self.buttons = [[None]*cols for _ in range(rows)]
        self.create_widgets()

    def create_widgets(self):
        for r in range(self.rows):
            for c in range(self.cols):
                button = tk.Button(self.master, text="", width=2, height=1)
                button.grid(row=r, column=c)
                self.buttons[r][c] = button

    def second_reveal(self, r, c):
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if i != r or j != c:
                    if 0 <= i < self.rows and 0 <= j < self.cols and j not in self.mine_grid[i] and self.buttons[i][j]["text"] == "":
                        amount_mines = self.count_mines(i, j)
                        if amount_mines == 0:
                            self.buttons[i][j].config(text=" ", state="disabled", bg="white")
                            self.second_reveal(i, j)
                        else:
                            self.buttons[i][j].config(text=amount_mines, state="disabled", bg="white")

    def count_mines(self, r, c):
        count = 0
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if 0 <= i < self.rows and 0 <= j < self.cols and j in self.mine_grid[i]:
                    count += 1
        return count

    def game_over(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if c in self.mine_grid[r]:
                    self.buttons[r][c].config(text="*", bg="red", state="disabled")
                else:
                    amount_mines = self.count_mines(r, c)
                    self.buttons[r][c].config(text=" " if amount_mines == 0 else amount_mines, state="disabled", bg="white")
                self.buttons[r][c].unbind("<Button-1>")
                self.buttons[r][c].unbind("<Button-3>")
        self.game_over_label.config(text="Game Over")
        self.game_over_label.grid(row=self.rows, column=0, columnspan=self.cols)

def show_leaderboard():
    # Hier können Sie die Logik zum Anzeigen der Bestenliste hinzufügen
    messagebox.showinfo("Bestenliste", "Hier wird die Bestenliste angezeigt.")

def start_game():
    rows = int(row_entry.get())
    cols = int(col_entry.get())
    loading_screen.destroy()
    root = tk.Tk()
    game = Minesweeper(root, rows, cols)
    root.mainloop()

# Ladebildschirm erstellen
loading_screen = tk.Tk()
loading_screen.title("Minesweeper Ladebildschirm")

tk.Label(loading_screen, text="Anzahl der Reihen:").grid(row=0, column=0)
row_entry = tk.Entry(loading_screen)
row_entry.grid(row=0, column=1)

tk.Label(loading_screen, text="Anzahl der Spalten:").grid(row=1, column=0)
col_entry = tk.Entry(loading_screen)
col_entry.grid(row=1, column=1)

start_button = tk.Button(loading_screen, text="Spiel starten", command=start_game)
start_button.grid(row=2, column=0, columnspan=2)

leaderboard_button = tk.Button(loading_screen, text="Bestenliste anzeigen", command=show_leaderboard)
leaderboard_button.grid(row=3, column=0, columnspan=2)

loading_screen.mainloop()