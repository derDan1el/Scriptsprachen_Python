import tkinter as tk
import random

def start_game_window(hautpfenster,rows,cols,mines):
    game_window = tk.Toplevel(hauptfenster)
    game_window.title("Minesweeper")
    Minesweeper(game_window,rows,cols,mines)
    
    
    
    
def create_start_window(hauptfenster):
    # Hauptfenster konfigurieren
    hauptfenster.geometry("500x500")
    hauptfenster.title("Minesweeper Einstellungen")
    
    int_Breite = tk.IntVar()
    int_Höhe = tk.IntVar()

    breite_textfeld = tk.Entry(hauptfenster, textvariable=int_Breite, width=10, font=('Arial', 12), fg='black')
    breite_textfeld.place(x=25,y=350)
    # Ein ttk-Label-Widget
    label_spielfeldgröße = tk.Label(hauptfenster, text="Spielfeldgröße")
    label_spielfeldgröße.place(x=50, y=25)
    
    
    label_spielfeldgröße = tk.Label(hauptfenster, text="Leicht: Spielfeld 8x8 Felder und 10 Minen")
    label_spielfeldgröße.place(x=75, y=60)
    
    label_spielfeldgröße = tk.Label(hauptfenster, text="Mittel: Spielfeld 16x16 Felder und 40 Minen")
    label_spielfeldgröße.place(x=75, y=110)

    label_spielfeldgröße = tk.Label(hauptfenster, text="Schwer: Spielfeld 30x16 Felder und 99 Minen")
    label_spielfeldgröße.place(x=75, y=160)
    
    label_spielfeldgröße = tk.Label(hauptfenster, text="Individuell: max. 30x30 Felder, max 800 Minen")
    label_spielfeldgröße.place(x=75, y=210)

    button_leicht = tk.Button(
        hauptfenster,
        text="Start",
        width=2,
        height=1,
        font=("Helvetica", 11, "bold"),
        bg="lightblue",
        fg="black",
        padx=7,
        pady=5,
        state="normal",
        relief="flat",
        bd=5,
        command=lambda: start_game_window(hauptfenster,8,8,10),
        anchor="center",
        cursor="hand2",
        highlightbackground="black",
        highlightthickness=1
    )
    button_leicht.place(x=25, y=50)
    
    button_mittel = tk.Button(
        hauptfenster,
        text="Start",
        width=2,
        height=1,
        font=("Helvetica", 11, "bold"),
        bg="lightblue",
        fg="black",
        padx=7,
        pady=5,
        state="normal",
        relief="flat",
        bd=5,
        command=lambda: start_game_window(hauptfenster,16,16,40),
        anchor="center",
        cursor="hand2",
        highlightbackground="black",
        highlightthickness=1
    )
    button_mittel.place(x=25, y=100)
    
    button_schwer = tk.Button(
        hauptfenster,
        text="Start",
        width=2,
        height=1,
        font=("Helvetica", 11, "bold"),
        bg="lightblue",
        fg="black",
        padx=7,
        pady=5,
        state="normal",
        relief="flat",
        bd=5,
        command=lambda: start_game_window(hauptfenster,30,16,99),
        anchor="center",
        cursor="hand2",
        highlightbackground="black",
        highlightthickness=1
    )
    button_schwer.place(x=25, y=150)
    
    button_individuell = tk.Button(
        hauptfenster,
        text="Start",
        width=2,
        height=1,
        font=("Helvetica", 11, "bold"),
        bg="lightblue",
        fg="black",
        padx=7,
        pady=5,
        state="normal",
        relief="flat",
        bd=5,
        command=lambda: start_game_window(hauptfenster,30,16,99),
        anchor="center",
        cursor="hand2",
        highlightbackground="black",
        highlightthickness=1
    )
    button_individuell.place(x=25, y=200)
    
    
    button_individuell = tk.Button(
        hauptfenster,
        text="Rekorde",
        width=5,
        height=2,
        font=("Helvetica", 11, "bold"),
        bg="lightgreen",
        fg="black",
        padx=7,
        pady=5,
        state="normal",
        relief="flat",
        bd=5,
        anchor="center",
        cursor="hand2",
        highlightbackground="black",
        highlightthickness=1
    )
    button_individuell.place(x=25, y=300)
    
    
    #individuelle textfellder
    
def on_entry_click(event):
    if entry.get() == 'Breite':
        entry.delete(0, "end")  # Löscht den Platzhaltertext
        entry.insert(0, '')  # Setzt den Cursor an den Anfang
        entry.config(fg='black')
        

    
    
def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Breite')
        entry.config(fg='grey')

def submit_text():
    entered_text = entry.get()
    print(f"Eingegebener Text: {entered_text}")
    # Hier können Sie den Text weiterverarbeiten oder speichern

    
    
    
    
class Minesweeper:
    def __init__(self, master, rows=10, cols=10, mines=90):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = []
        self.mine_grid = [[] for _ in range(rows)] #leere liste für die mines 
        self.game_over_label = tk.Label(master, text="", font=("Helvetica", 24), fg="red")
        self.create_widgets()
        self.place_mines()

    def create_widgets(self):
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                btn = tk.Button(self.master, width=1, height=1,relief="flat", highlightbackground="black", highlightthickness=1)
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
                
    def pick_color(self,amount_mines):
        if amount_mines == 1:
            return "blue"
        elif amount_mines == 2:
            return "green"
        elif amount_mines == 3:
            return "red"
        elif amount_mines == 4:
            return "purple"
        elif amount_mines == 5:
            return "maroon"
        elif amount_mines == 6:
            return "turquoise"
        elif amount_mines == 7:
            return "black"
        elif amount_mines == 8:
            return "gray"
        else:
            return "black" 

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
                color = self.pick_color(amount_mines)
                self.buttons[r][c].config(text=amount_mines,fg=color,bg="white")
                print(self.buttons[r][c].cget("fg"))

          
    def second_reveal(self, r, c):
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if i != r or j != c:
                    if 0 <= i < self.rows and 0 <= j < self.cols and j not in self.mine_grid[i] and self.buttons[i][j]["text"] == "":
                        amount_mines = self.count_mines(i, j)
                        if amount_mines == 0:
                            self.buttons[i][j].config(text=" ",bg="white")
                            self.second_reveal(i, j)
                        else:
                            color = self.pick_color(amount_mines)
                            self.buttons[i][j].config(text=amount_mines ,bg="white",fg=color)
                            
        
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
        self.game_over_label.config(text="Game Over")
        self.game_over_label.grid(row=self.rows, column=0, columnspan=self.cols)

    
    
if __name__ == "__main__":
    hauptfenster = tk.Tk()
    create_start_window(hauptfenster)
    # Hauptschleife starten
    hauptfenster.mainloop()
    

