import random;
zufallszahl = random.randint(0,100)
print(zufallszahl)

def raten():
    print("Raten Sie eine Zahl zwischen 0 und 100")
    zahl = input("Ihre Zahl: ")
    try:
        zahl = int(zahl)
    except ValueError:
        print("Das war keine Zahl")
        return raten()
    
    if(zahl == zufallszahl):
        print("Richtig geraten")
        return 
    else:
        print("Leider falsch")
        if( zufallszahl > zahl):
            print("Die gesuchte Zahl ist größer")
        else:
            print("Die gesuchte Zahl ist kleiner")
        return raten()
    

raten()