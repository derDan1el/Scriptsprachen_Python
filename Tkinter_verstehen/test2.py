import tkinter as tk

def zeige_bild():
    Button1.config(image=bomb_image)

root = tk.Tk()
root.title("Mein erstes Fenster")
root.geometry("400x300")

# Bild laden
bomb_image = tk.PhotoImage(file="Tkinter_verstehen/bombn.png")

# Button ohne Bild erstellen
Button1 = tk.Button(root, text="")
Button1.pack()

# Button zum Anzeigen des Bildes
zeige_bild_button = tk.Button(root, text="Bild anzeigen", command=zeige_bild)
zeige_bild_button.pack()

root.mainloop()