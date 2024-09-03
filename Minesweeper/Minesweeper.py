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
        self.game_over_label = tk.Label(master, text="", font=("Helvetica", 24), fg="red")
        self.create_widgets()
        self.first_decision = True
        self.place_mines()

            
    def create_widgets(self):
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                btn = tk.Button(self.master, width=1, height=1)
                btn.bind("<Button-1>", lambda e, r=r, c=c:self.fsreveal(r, c) if self.first_decision == True else self.first_reveal(r, c))  # Linksklick
                btn.bind("<Button-3>", lambda e, r=r, c=c: self.right_click(r, c)) #rechtsklick was passiert
                btn.grid(row=r, column=c)#button wird in grid platziert ort 
                row.append(btn) #button wird in row hinzugefügt diese 2 zeilen sind für die referenz auf den button
            self.buttons.append(row) #row wird in buttons hinzugefügt
    
    def right_click(self, r, c):
        if self.buttons[r][c]["text"] == "":
            self.buttons[r][c].config(text="M")
        elif self.buttons[r][c]["text"] == "M":
            self.buttons[r][c].config(text="?")
        elif self.buttons[r][c]["text"] == "?":
            self.buttons[r][c].config(text="")
        
    
    def fsreveal(self, r, c):
        self.first_decision = False
        if c in self.mine_grid[r]:
            self.mine_grid[r].remove(c)
            new_mine_found = False
            while not new_mine_found:
                r1 = random.randint(0, self.rows - 1)
                c1 = random.randint(0, self.cols - 1)
                if (c1 != c or r1 != r) and c1 not in self.mine_grid[r1]:
                    self.mine_grid[r1].append(c1)
                    new_mine_found = True
        self.first_reveal(r, c)
                    


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
                    self.buttons[r][c].config(text="*", bg="red",state="disabled")
                else:
                    amount_mines = self.count_mines(r, c)
                    self.buttons[r][c].config(text= " " if amount_mines == 0 else amount_mines,state="disabled",bg="white")
                self.buttons[r][c].unbind("<Button-1>")
                self.buttons[r][c].unbind("<Button-3>")
        self.game_over_label.config(text="Game Over")
        self.game_over_label.grid(row=self.rows, column=0, columnspan=self.cols)
    
    
    

if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()