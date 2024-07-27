



def Prüfziffer_berechnen(ziffernfolge):
    s =0
    iterator = 1
    if(len(str(ziffernfolge)) != 9):
        return "Fehler: Die Ziffernfolge muss 9-stellig sein!"
    else:
        for i in ziffernfolge:
            if(not i.isdigit()):
                return "Fehler: Die Ziffernfolge darf nur Zahlen enthalten!"
            else:
                s += int(i)*iterator
                iterator += 1
                
        z_10 = s%11
        if(z_10 == 10):
            return "X"
        else:
            return z_10
        


#print(Prüfziffer_berechnen(input("Geben Sie eine 9-stellige Ziffernfolge ein: ")))

def zeitumrechnung(sekunden):
    sekunden = int(sekunden)
    if(sekunden < 0):
        return "Fehler: Die Anzahl der Sekunden muss größer oder gleich 0 sein!"
    else:
        tage = sekunden//86400
        sekunden = sekunden%86400
        stunden = sekunden//3600
        sekunden = sekunden%3600
        minuten = sekunden//60
        sekunden = sekunden%60
    
        return str(tage) + " Tage, " + str(stunden) + " Stunden, " + str(minuten) + " Minuten und " + str(sekunden) + " Sekunden"    



print(zeitumrechnung(input("Geben Sie eine Anzahl von Sekunden ein: ")))