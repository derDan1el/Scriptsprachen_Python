import tkinter as tk
import random
import os


#--------------------------nachdem man das Spiel zurücksetzt oder im Titelscreen aufgerufen
def start_game_window(hautpfenster,rows,cols,mines):
    game_window = tk.Toplevel(hauptfenster)
    game_window.title("Minesweeper")
    Minesweeper(game_window,rows,cols,mines)
    
    
    
#--------------------------Alles zu dem Titelscreen um die Settings einzustellen
def create_start_window(hauptfenster):
    # Hauptfenster konfigurieren
    hauptfenster.title("Minesweeper Einstellungen")
    hauptfenster.geometry("500x500")
    
    fehlermeldung_label = tk.Label(hauptfenster, text="", font=('Arial', 12), fg='red')
    
    str_Breite = tk.StringVar()
    str_Höhe = tk.StringVar()
    str_Minen = tk.StringVar()

    breite_textfeld = tk.Entry(hauptfenster, textvariable=str_Breite, width=10, font=('Arial', 12), fg='black')
    breite_textfeld.place(x=75,y=250)
    
    label_Breite = tk.Label(hauptfenster, text="Reihen:")
    label_Breite.place(x=25, y=250)
    
    höhe_textfeld = tk.Entry(hauptfenster, textvariable=str_Höhe, width=10, font=('Arial', 12), fg='black')
    höhe_textfeld.place(x=75,y=275)
    
    label_Höhe = tk.Label(hauptfenster, text="Spalten:")
    label_Höhe.place(x=20, y=275)

    Minen_textfeld = tk.Entry(hauptfenster, textvariable=str_Minen, width=10, font=('Arial', 12), fg='black')
    Minen_textfeld.place(x=75,y=300)
    
    label_Minen = tk.Label(hauptfenster, text="Minen:")
    label_Minen.place(x=25, y=300)
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


#--------------------------Buttons für die Schwierigkeitsgrade und individuell ... ein wenig herumgespielt mit den Buttons was es denn so gibt
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
        command=lambda: start_individuell(),
        anchor="center",
        cursor="hand2",
        highlightbackground="black",
        highlightthickness=1
    )
    button_individuell.place(x=25, y=200)
    
    

    
#--------------------------Da individuell bestimmte Bedingungen erfüllen muss wie zb mehr felder als Minen oder keine negativen zahlen...
    def start_individuell():
        try:
            breite = int(str_Breite.get().lstrip("0"))
            höhe = int(str_Höhe.get().lstrip("0"))
            minen = int(str_Minen.get().lstrip("0"))
            
            if breite > 30 or höhe > 30 or breite < 1 or höhe < 1:
                fehlermeldung_label.config(text="Breiten -und Höhenwerte zwischen 1 und 30 sind erlaubt")
                fehlermeldung_label.place(x=25, y=330)
                hauptfenster.after(2500, lambda: fehlermeldung_label.place_forget())
                
            elif breite * höhe <= minen + 2: # +2 weoil +1 bedeutet es gibt ein nicht minenfeld wird eh bei der ersten entscheidung "gefunden"
                fehlermeldung_label.config(text="zu viele Minen für das Spielfeld")
                fehlermeldung_label.place(x=25, y=330)
                hauptfenster.after(2500, lambda: fehlermeldung_label.place_forget())  # Label nach 3 Sekunden entfernen
            elif minen > 800:
                fehlermeldung_label.config(text="Die Anzahl der Minen darf 800 nicht überschreiten")
                fehlermeldung_label.place(x=25, y=330)
                hauptfenster.after(2500, lambda: fehlermeldung_label.place_forget())
            else:
                start_game_window(hauptfenster,breite,höhe,minen)
        except tk.TclError:  # spezifischer Fehler für ungültige Eingabe in IntVar
            fehlermeldung_label.config(text="Keine Zahl")
            fehlermeldung_label.place(x=25, y=330)
            
        except ValueError:  # Fehler bei der Umwandlung in eine Ganzzahl
                fehlermeldung_label.config(text="Keine gültige Zahl")
                fehlermeldung_label.place(x=25, y=330)
                hauptfenster.after(2500, lambda: fehlermeldung_label.place_forget())  # Label nach 2,5 Sekunden entfernen
                

#--------------------------Rekorde anzeigem... methode wird aufgerufen beim "Rekorde" button
    def open_rekord_window():
        
        lines = []
        with open("Rekorde.txt", "r") as file:
            lines = file.readlines()
        
        #fenster settings
        rekord_window = tk.Toplevel(hauptfenster)
        rekord_window.title("Rekorde")
        rekord_window.geometry("600x400")
        
        
        #die "Tabelle" erstellen mit leicht mittel schwer individuell
        label_leicht = tk.Label(rekord_window, text="Leicht", font=("Helvetica", 12, "bold"), borderwidth=0, relief="groove")
        label_leicht.place(x=75, y=10)

        label_mittel = tk.Label(rekord_window, text="Mittel", font=("Helvetica", 12, "bold"), borderwidth=0, relief="groove")
        label_mittel.place(x=175, y=10)

        label_schwer = tk.Label(rekord_window, text="Schwer", font=("Helvetica", 12, "bold"), borderwidth=0, relief="groove")
        label_schwer.place(x=275, y=10)

        label_individuell = tk.Label(rekord_window, text="Individuell", font=("Helvetica", 12, "bold"), borderwidth=0, relief="groove")
        label_individuell.place(x=375, y=10)
        
        krone_bild = tk.PhotoImage(file=r"Krone.png")
        
        label_Krone = tk.Label(rekord_window,image = krone_bild)
        label_Krone.image = krone_bild
        label_Krone.place(x=10, y=30)
        
        #herausfindne wie viele rekorde es bei der jeweiligen schwierigkeit gibt
        nLeicht,nMittel,nSchwer,nIndividuell = [],[],[],[]
        
        if os.path.isfile("Rekorde.txt"):
            with open("Rekorde.txt", "r") as file: #r liest
                nLeicht = file.readline().split()[1:] #lies nur die zeiten aus der zeile
                nMittel = file.readline().split()[1:]
                nSchwer = file.readline().split()[1:]
                nIndividuell = file.readline().split()[1:]
        
        #die rekorde in die labels schreiben und ordentlich untereinander aufreihen:
        for i in range(len(nLeicht)):
             tk.Label(rekord_window, text=nLeicht[i], font=("Helvetica", 12, "bold"), borderwidth=0, relief="groove").place(x=75, y=15+ (i+1) * 30)
        
        for i in range(len(nMittel)):
            tk.Label(rekord_window, text=nMittel[i], font=("Helvetica", 12, "bold"), borderwidth=0, relief="groove").place(x=175, y=15+ (i+1) * 30)

        for i in range(len(nSchwer)):
             tk.Label(rekord_window, text=nSchwer[i], font=("Helvetica", 12, "bold"), borderwidth=0, relief="groove").place(x=275, y=15+ (i+1) * 30)
        
        for i in range(len(nIndividuell)):
            tk.Label(rekord_window, text=nIndividuell[i], font=("Helvetica", 12, "bold"), borderwidth=0, relief="groove").place(x=375, y=15+ (i+1) * 30)
    
    
    button_rekord = tk.Button(
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
        command=lambda: open_rekord_window(),
        anchor="center",
        cursor="hand2",
        highlightbackground="black",
        highlightthickness=1
    )
    button_rekord.place(x=25, y=400)
    
    


    
    
    
    
class Minesweeper:
    def __init__(self, master, rows=10, cols=10, mines=90):
        self.master = master
        bg=master.cget("bg")
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.marked_mines = 0
        self.buttons = []
        self.mine_grid = [[] for _ in range(rows)] #leere liste für die mines
        self.rekordfile = "Rekorde.txt"
        self.bomb_picture = tk.PhotoImage(file="reset_button.png")
        
        self.game_over_label = tk.Label(master, text="", font=("Helvetica", 20), fg="red")
        self.game_won_label = tk.Label(master, text="", font=("Helvetica", 20), fg="green")
        
        self.stopwatch_label = tk.Label(master, text="00:00:00", font=("Helvetica", 14), fg="black")
        self.stopwatch_label.grid(row=0, column=0, columnspan=2)
        
        #self.button_cheat = tk.Button(master,text = "cheat",command = lambda: self.cheat())
        #self.button_cheat.grid(row = 0, column = 4, columnspan = 5)
        
        self.button_KI = tk.Button(master,text = "KI Move",command = lambda:self.KI_Move() )
        self.button_KI.grid(row = 0, column = 1, columnspan = 5)
        
        self.reset_button = tk.Button(master,image=self.bomb_picture,activebackground=bg,command=lambda: self.reset(self.master,self.rows,self.cols,self.mines),borderwidth=0,highlightthickness=0)
        self.reset_button.grid(row=0, column=self.cols//2 +1, columnspan=1) 
        
        self.count_marks_label = tk.Label(master, text=f"{self.mines}", font=("Helvetica", 14), fg="black")
        self.count_marks_label.grid(row=0, column=self.cols-1, columnspan=1)
        
        self.create_widgets()
        self.first_decision = True
        self.place_mines()
        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.schwierigkeit = self.get_schwierigkeit()
        
        self.KI_mines = []
        self.not_revealed_safe_fields = []
        
        
    
    def KI_Move(self):
        if self.first_decision:
            self.lustiges_feature()
            self.button_KI.config(state="disabled")
            self.check_KI_move_avail()
            self.__KI_helper_move()
        else:
            try:
                tup = self.not_revealed_safe_fields.pop(0)
                self.first_reveal(tup[0],tup[1])
            except:
                self.button_KI.config(state="disabled")
            
        
        
#######################################Lustiges Feature: gleich am Anfang Ki Move auswählen#############################################################
    def lustiges_feature(self):
        self.button_KI.config(state="disabled")
        self.first_decision = False
        for r in range(self.rows):
            for c in range(self.cols):
                self.buttons[r][c].unbind("<Button-1>")
        # Erstellen eines neuen Fensters für den Ladebalken
        self.progress_window = tk.Toplevel(self.master)
        self.progress_window.title("Ladebalken")    
        # Erstellen des Canvas für den Ladebalken
        self.canvas = tk.Canvas(self.progress_window, width=300, height=30, bg='white')
        self.canvas.pack(pady=20)   
        # Erstellen des Ladebalkens
        self.progress_bar = self.canvas.create_rectangle(0, 0, 0, 30, fill='blue')
        self.progressbar = tk.Label(self.progress_window, text="extremely difficult math computations!!!", font=("Helvetica", 14), fg="black")
        self.progressbar.pack(pady=10)  
        # Methode zum Aktualisieren des Fortschritts
        def update_progress():
            current_width = self.canvas.coords(self.progress_bar)[2]
            if current_width < 300:
                new_width = current_width + 10#3  # Erhöht die Breite des Ladebalkens
                self.canvas.coords(self.progress_bar, 0, 0, new_width, 30)
                self.progress_window.after(100, update_progress)  # Aktualisiert den Fortschritt alle 100 ms
                if current_width == 150:
                    self.progressbar.config(text="Intense Calculations!!!!!!!")
                if current_width == 225:
                    self.progressbar.config(text="ALMOST FINISHEDD!!!!!!!!")   
            else:
                self.progress_window.destroy()  # Schließt das Fenster, wenn der Fortschritt 100% erreicht
                for r in range(self.rows):
                    for c in range(self.cols):
                        self.buttons[r][c].bind("<Button-1>", lambda e, r=r, c=c: self.fsreveal(r, c) if self.first_decision == True else self.first_reveal(r, c))
                self.fsreveal(0,0)
                self.button_KI.config(state="normal")
        # Startet die Aktualisierung des Fortschritts
        update_progress()
        
        
        
        
        #Minen Finden
####################################################################################################
    #ist text eine zahl?
    def is_number(self, str):
        try:
            int(str)
            return True
        except ValueError:
            return False
        
    #ein button finden mit einer zahl:
    def find_number(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.is_number(self.buttons[r][c]["text"]):
                    self.get_unrevealed_neighbours(r,c)
                
    #finde heraus welche die unrevealed neighbours sind
    def get_unrevealed_neighbours(self,r,c):
        tup = []
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if 0 <= i < self.rows and 0 <= j < self.cols and self.buttons[i][j]["bg"] == "lightgrey":
                    tup.append((i,j))
        return self.obvious_mines_check(r,c,tup)
    
    
    #Anzahl der unrevealed neighbours gleich der anzahl der bombs around?
    def obvious_mines_check(self,r,c,tupels):
        if int(self.buttons[r][c]["text"]) == len(tupels):
            for tup in tupels:
                if tup not in self.KI_mines:
                    self.KI_mines.append(tup)
            
            
            
            #find safe fields 
####################################################################################################

    def bombs_around(self,r,c):
        tupel = []
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if 0 <= i < self.rows and 0 <= j < self.cols and (i,j) in self.KI_mines:
                    tupel.append((i,j))
        return tupel
    
    def get_unrevealed_neighbours_tupels(self,r,c):
        tup = []
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if 0 <= i < self.rows and 0 <= j < self.cols and self.buttons[i][j]["bg"] == "lightgrey":
                    tup.append((i,j))
        return tup
    

    def find_safe_fields(self):
        for r in range(self.rows):
            for c in range(self.cols):
                all_neighbours = self.get_unrevealed_neighbours_tupels(r,c)
                known_bomb_neighbours = self.bombs_around(r,c)
                #muss ne zahl sein#es müssen so viele bombs around sein wie die zahl#es muss mehr unrevealed neighbours geben als bombs around
                if self.is_number(self.buttons[r][c]["text"]) and int(self.buttons[r][c]["text"]) == len(known_bomb_neighbours) < len(all_neighbours):
                    for tup in all_neighbours:
                        if tup not in known_bomb_neighbours and tup not in self.not_revealed_safe_fields:
                            self.not_revealed_safe_fields.append(tup)
                            

    #geöffnete felder welche sich in not_revealed_safe_fields befinden entfernen:
####################################################################################################
    def remove_opened_fields(self):
        for tup in self.not_revealed_safe_fields:
            if self.buttons[tup[0]][tup[1]]["bg"] != "lightgrey":
                self.not_revealed_safe_fields.remove(tup)


    #Ki move button verfügbar?
####################################################################################################

    def check_KI_move_avail(self):
        if self.first_decision:
            return True
        else:
            self.remove_opened_fields()
            self.find_number()
            self.find_safe_fields()
            self.remove_opened_fields()
            if len(self.not_revealed_safe_fields) > 0:
                return True
            else: 
                return False
            
    
####################################################################################################
    
    
    
    
    
    
    
    #das können sie benutzen es gibt auc heinen cheat button um das spiel schnell zu gewinne nund die rekorde zu testen: 
    def cheat(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if c not in self.mine_grid[r] and self.buttons[r][c]["bg"] == "lightgrey":
                    self.buttons[r][c].event_generate("<Button-1>")
                    return
    
    def get_schwierigkeit(self):
        if self.rows == 8 and self.cols == 8 and self.mines == 10:
            return "Leicht"
        elif self.rows == 16 and self.cols == 16 and self.mines == 40:
            return "Mittel"
        elif self.rows == 30 and self.cols == 16 and self.mines == 99:
            return "Schwer"
        else:
            return "Individuell"
        
    #reset button
    def reset(self,master, rows, cols, mines):
        self.game_over_label.config(text="")
        self.game_won_label.config(text="")
        Minesweeper(master, rows, cols, mines)
    
    #stopuhr oben links im programm
    def update_stopwatch(self):
        if self.running:
            self.milliseconds += 1
            if self.milliseconds == 100:
                self.milliseconds = 0
                self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            
            time_value = f"{self.minutes:02}:{self.seconds:02}:{self.milliseconds:02}"#02 formatierungstring mit 2 stellen und führenden nullen
            self.stopwatch_label.config(text=time_value)
            self.master.after(10, self.update_stopwatch) #10ms verzögerung
            #after ist eine methode von tkinter und muss also auf master aufgerufen werden

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.update_stopwatch()

    def right_click(self, r, c):
        if self.buttons[r][c]["text"] == "":
            self.buttons[r][c].config(text="M")
            self.marked_mines += 1
            self.count_marks_label.config(text=f"{self.mines - self.marked_mines}")
            self.buttons[r][c].unbind("<Button-1>")
        elif self.buttons[r][c]["text"] == "M":
            self.buttons[r][c].config(text="?")
            self.marked_mines -= 1
            self.count_marks_label.config(text=f"{self.mines - self.marked_mines}")
            self.buttons[r][c].bind("<Button-1>", lambda e, r=r, c=c: self.fsreveal(r, c) if self.first_decision == True else self.first_reveal(r, c))
        elif self.buttons[r][c]["text"] == "?":
            self.buttons[r][c].config(text="")


    def count_mines(self, r, c):
        count = 0
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if 0 <= i < self.rows and 0 <= j < self.cols and j in self.mine_grid[i]:
                    count += 1
        return count
    
    #fsreveal ist die aller erste entscheidung im spiel damit es keine mine ist wird eine neue mine an einer anderen stelle platziert
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
        self.start_stopwatch()
        self.first_reveal(r, c)

    #erstellt alle buttons
    def create_widgets(self):
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                btn = tk.Button(self.master,relief="flat",width = 1,height = 1,bg ="lightgrey", highlightbackground="black", highlightthickness=1,font=("Helvetica", 12, "bold"))
                btn.bind("<Button-1>", lambda e, r=r, c=c:self.fsreveal(r, c) if self.first_decision == True else self.first_reveal(r, c))  # Linksklick
                btn.bind("<Button-3>", lambda e, r=r, c=c: self.right_click(r, c)) #rechtsklick was passiert
                btn.grid(row=r+1, column=c)#button wird in grid platziert ort 
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
    
    # für die zahlen auf den feldern
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
        
    #checkt ob button aktiviert sein darf
    def __KI_helper_move(self):
        if self.check_KI_move_avail():
                self.button_KI.config(state="normal")
        else:
                self.button_KI.config(state="disabled")

    #erstes aufdecken (nach der ersten entscheidung)
    def first_reveal(self, r, c):
        if c in self.mine_grid[r]:
            self.buttons[r][c].config(text ="💣")
            self.game_over()
        else:
            amount_mines = self.count_mines(r, c)
            if amount_mines == 0:
                self.buttons[r][c].config(text="", bg="white")
                self.second_reveal(r, c)
                
                self.__KI_helper_move()
                
            else:
                color = self.pick_color(amount_mines)
                self.buttons[r][c].config(text=amount_mines,fg=color,bg="white")
                
                self.__KI_helper_move()

        self.check_win()

    #wenn es keine minen in der nähe gibt wird das hier aufgerufen um mehr aufzudecken
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
    
    
    #vergleiche und ersetze die zeiten in der rekorde datei
    def vergleiche_und_ersetze(self,line,zeit):
        array = line.split(" ")[1:-1] #das erste element brauche ich nicht "Leicht bsp"
        added = False
        for i in range(len(array)):
            if zeit < array[i]: #wenn die zeit kleiner ist als die zeit in der liste
                array.insert(i,zeit) #dann füge die zeit an der stelle ein alle anderen nachfolgenden elemente werden nach rechts verschoben
                added = True
                break
        if len(array) > 5:
            array.pop() #das letzte element entfernen
        if not added and len(array) < 5:
            array.append(zeit)
        array.append("\n")
        return " ".join(array) #array in string umwandeln
            
    #rekord schreiben
    def write_rekord(self):
        if os.path.isfile(self.rekordfile):
            with open(self.rekordfile, "r+") as file: #r+ liest und schreibt
                lines = file.readlines()
                index = 0
                if self.schwierigkeit == "Mittel":
                    index = 1
                elif self.schwierigkeit == "Schwer":
                    index = 2
                elif self.schwierigkeit == "Individuell":
                    index = 3
                
                
                if len(lines[index].split()) == 1: # wennn nur "Leicht" drinne steht in zeile 1 eifnach adden
                    lines[index] = lines[index].strip() + (f" {self.minutes:02}:{self.seconds:02}:{self.milliseconds:02} \n")
                    file.seek(0)
                    file.writelines(lines)
                    
                else:
                    new_rekord_line =lines[index].split()[0] + " "+ self.vergleiche_und_ersetze(lines[index],f"{self.minutes:02}:{self.seconds:02}:{self.milliseconds:02}")
                    lines[index] = new_rekord_line
                    file.seek(0)
                    file.writelines(lines)
        
        else:
            with open(self.rekordfile, "w") as file:
                file.write("Leicht \n")
                file.write("Mittel \n")
                file.write("Schwer \n")
                file.write("Individuell \n")
            self.write_rekord()
                
                
                        
                        
                    

                
    def game_over(self):
        self.game_over_label.config(text="Game Over")
        self.game_over_label.grid(row=self.rows+1, column=0, columnspan=self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                if c in self.mine_grid[r]:
                    self.buttons[r][c].config(text="💣",bg = "red")
                self.buttons[r][c].unbind("<Button-1>")
                self.buttons[r][c].unbind("<Button-3>")
                self.running = False
    
    def check_win(self):
        won = True
        for r in range(self.rows):
            for c in range(self.cols):
                if self.buttons[r][c]["bg"] == "lightgrey" and c not in self.mine_grid[r]:
                    won = False
                    return 
        if won:
            self.game_won_label.config(text="You Win!",fg="green")
            self.game_won_label.grid(row=self.rows+1, column=0, columnspan=self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    if c in self.mine_grid[r]:
                        self.buttons[r][c].config(text="💣",bg = "lightgreen")
                    self.buttons[r][c].unbind("<Button-1>")
                    self.buttons[r][c].unbind("<Button-3>")
                    self.running = False
            self.write_rekord()

    
if __name__ == "__main__":
    hauptfenster = tk.Tk()
    create_start_window(hauptfenster)
    # Hauptschleife starten
    hauptfenster.mainloop()
    

