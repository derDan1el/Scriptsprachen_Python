


kollektion = [i**2 for i in range(10)]
tupel = {i : i**2 for i in range(10)}
#print(kollektion)
#print(tupel)


def collatzProblem():
    
    for i in range(1, 1000):
        n = int(i)
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else :
                n = 3 * n + 1
            print(n)
        print("-------------------------------")
        
#collatzProblem()

def tolleresprint(*mehrere_argumente):
    for element in mehrere_argumente:
        print(str(element),end=" ")

#tolleresprint( (1,23,3),{4,565,3}, [1234,345,56],1,2,"ende",True)

a  = 5
def seiteneffekt():
    global a
    a += 10

print(a)
seiteneffekt()
print(a)

def liste_aendern(liste):
    liste.append(4)

meine_liste = [1, 2, 3]
liste_aendern(meine_liste)
print(meine_liste)  # Ausgabe: [1, 2, 3, 4]


def beispiel_lok_namesraum():
    x_a = [0]
    def add_innere():
        x_a +=1
        print("Innere Funktion: ", x)
    def sub_innere():
        x_a -=1
        print("Innere Funktion: ", x)
    def get_innere():
        print("Innere Funktion: ", x)
    return(add_innere, sub_innere)

add,sub = beispiel_lok_namesraum()


    
