import os




def write_rekord():
    if os.path.exists("rekord.txt"):
        with open("rekord.txt", "r+") as file:
            lines = file.readlines()
            

    
    
    
    
    
    
    else:
        with open(rekordfile, "w") as file:
            file.write("Leicht\n, Mittel\n, Schwer\n, Individuell\n")
            if schwierigkeit == "Leicht":
                file.write(f"{minutes:02}:{seconds:02}:{milliseconds:02}\n")