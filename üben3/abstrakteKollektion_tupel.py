import csv
import datetime
import sys
import numpy
import pandas
import time
import random



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
        x_a[0] +=1
        print("Innere Funktion: ", x_a)
    def sub_innere():
        x_a[0] -=1
        print("Innere Funktion: ", x_a)
    def get_innere():
        print("Innere Funktion: ", x_a)
    return(add_innere, sub_innere,get_innere) # Rückgabe der Funktionen

add,sub,get_innere = beispiel_lok_namesraum()
add()
sub()
get_innere()

summe = lambda x, y : x + y

print(summe(2,3))
liste = [22.4 , 21.3, 23.4]

print(list(map(lambda x: round(x), liste)))
# Liste (viel Speicherverbrauch)
a = [i*i for i in range(10)]
print(a)  # Ausgabe: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Generator (wenig Speicherverbrauch)
b = (i*i for i in range(10))
print(b)  # Ausgabe: <generator object <genexpr> at 0x034311E0>

# Zugriff auf die Elemente des Generators
for n in b:
    print(n, end=' ')  # Ausgabe: 0 1 4 9 16 25 36 49 64 81

datei = open("/home/daniel/Scriptsprachen_Python/VL4/neue_textdatei.txt","w")
datei.write("Hallo Welt\n")
datei.write("Hallo Welt\n")
datei.flush()
datei.write(str(datetime.datetime.now()) + "\n")
datei.close()   

datei = open("/home/daniel/Scriptsprachen_Python/VL4/neue_textdatei.txt","r")
x = datei.readline()
print(x)
datei.close()

l = [1, 2, 3]
with open('/home/daniel/Scriptsprachen_Python/VL4/test.txt', 'w') as output:
    output.write(f'Liste: {l}, 1tes Element: {l[0]}, Summe: {l[0] + l[1] + l[2]}')

    
print(len(sys.argv))
print(type(sys.argv))

for arg in sys.argv:
    print(arg, end='\n')



import time

# Gibt das aktuelle Datum und die Uhrzeit als lesbare Zeichenkette aus
print(time.asctime())

# Gibt die aktuelle Zeit in UTC als struct_time-Objekt aus
print(time.gmtime())

# Erstellt eine eigene Zeitstruktur (manuell) und gibt sie aus
custom_gmtime = time.struct_time((2016, 4, 22, 6, 15, 6, 4, 113, 0))
print(custom_gmtime)

# Gibt die aktuelle lokale Zeit als struct_time-Objekt aus
print(time.localtime())

# Erstellt eine eigene Zeitstruktur (manuell) für die lokale Zeit und gibt sie aus
custom_localtime = time.struct_time((2016, 4, 22, 8, 16, 30, 4, 113, 1))
print(custom_localtime)

# Gibt die aktuelle Zeit in Sekunden seit dem 1. Januar 1970 aus (Unix-Zeit)
print(time.time())

# Speichert den aktuellen Zeitstempel
t = time.time()

# Pausiert das Programm für eine Sekunde
time.sleep(1)

# Gibt die Differenz in Sekunden zwischen dem aktuellen Zeitpunkt und dem gespeicherten Zeitpunkt aus
print(time.time() - t)


print('die fabelhafte Welt der Pythonprogrammierung'.capitalize())

#
#Zusammenfassung der Unterschiede und Verwendungszwecke:
#Liste: Geordnete, veränderbare Sammlung von Elementen. Benutzen, wenn die Reihenfolge wichtig ist und die Daten verändert werden sollen.
#Tupel: Geordnete, unveränderbare Sammlung von Elementen. Benutzen, wenn die Reihenfolge wichtig ist und die Daten nicht verändert werden sollen.
#Set: Ungeordnete, veränderbare Sammlung von eindeutigen Elementen. Benutzen, wenn nur einzigartige Elemente benötigt werden und die Reihenfolge keine Rolle spielt.
#Dictionary: Ungeordnete Sammlung von Schlüssel-Wert-Paaren. Benutzen, wenn du Werte durch eindeutige Schlüssel referenzieren musst.



print(random.randint(1, 10))

A = numpy.array([[1, 5], [1.5, 7.501]])

# Berechnen der Inversen
A_inv = numpy.linalg.inv(A)

print("Inverse der Matrix A:\n", A_inv)
