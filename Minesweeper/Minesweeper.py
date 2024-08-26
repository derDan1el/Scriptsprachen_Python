import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows=10, cols=10, mines=10):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = []
        self.mine_grid = [[] for _ in range(rows)] #leere liste für die mines 
        self.create_widgets()
        self.place_mines()

    def create_widgets(self):
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                btn = tk.Button(self.master, width=2, height=1)
                btn.bind("<Button-1>", lambda e, r=r, c=c: self.first_reveal(r, c))  # Linksklick
                btn.bind("<Button-3>", lambda e, r=r, c=c: self.mark_mine(r, c)) #rechtsklick was passiert
                btn.grid(row=r, column=c)#button wird in grid platziert ort 
                row.append(btn) #button wird in row hinzugefügt diese 2 zeilen sind für die referenz auf den button
            self.buttons.append(row) #row wird in buttons hinzugefügt

    def place_mines(self):
        placed_mines = 0
        while placed_mines < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if c not in self.mine_grid[r]:
                self.mine_grid[r].append(c)
                placed_mines += 1
                

    def first_reveal(self, r, c):
        if c in self.mine_grid[r]:
            self.buttons[r][c].config(text="*", bg="red", state="disabled")
            self.game_over()
        else:
            amount_mines = self.count_mines(r, c)
            if amount_mines == 0:
                self.buttons[r][c].config(text=" ", state="disabled", bg="white")
                self.second_reveal(r, c)
            else:
                self.buttons[r][c].config(text=amount_mines, state="disabled",bg="white")

    def second_reveal(self, r, c):
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if i != r or j != c:
                    if 0 <= i < self.rows and 0 <= j < self.cols and j not in self.mine_grid[i] and self.buttons[i][j]["text"] == "":
                        amount_mines = self.count_mines(i, j)
                        if amount_mines == 0:
                            self.buttons[i][j].config(text=" ", state="disabled",bg="white")
                            self.second_reveal(i, j)
                        else:
                            self.buttons[i][j].config(text=amount_mines, state="disabled",bg="white")
        
    def mark_mine(self, r, c):
        self.buttons[r][c].config(text="M")

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
                        self.buttons[r][c].config(text="*", bg="red")
            print("Game Over")

if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()