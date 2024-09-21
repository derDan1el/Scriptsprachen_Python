

print(
    (True+1)**2 # true = 1
)


cool = ["apfel", "birne", "banane"]


for arsch in cool:
    print(arsch)


for i in range(0, len(cool)):
    print(cool[i], end = " ")

for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(5, 10, 2):
    print("      .    ")

fib1 = 1
fib2 = 1
for i in range(10):
    print(fib2, end=" ")
    tmp = fib2
    fib2 = fib1 + fib2
    fib1 = tmp


wort = input("Gib ein Wort ein: ")

for buchstabe in wort:
    print(buchstabe, end=" ")

anzahl =0
for buchstabe in wort:
    if buchstabe in "aeiouAEIOU":
        anzahl +=1

print(anzahl)

while(True):
    try:
        zahl = int(input("Gib eine Zahl ein: "))
        print(zahl)
        break
    except ValueError: # spezifischer error (ValueError)    
        print("Das war keine Zahl")
    except: # allgemeiner error
        pass    # do nothing



print(int("1010", 2)) # 2er System



print(int("1010", 4)) # 2er System



#map funktion wendet eine funktion auf jedes element einer liste / kollektion an
#beispiel:

print("längen")
result = map(len, ["hallo", "welt", "test"]) # gibt die länge der wörter zurück
print(list(result))


print("längen")



def quersummen(*zahlen):
    for zahl in zahlen:
        summe = 0
        for ziffer in str(zahl):
            summe += int(ziffer)
        print(summe)


print(quersummen(123, 456, 789, 101112))

print("hi")







#try:
#    datei = open("test.txt")
#    print(datei.read())

#finally: # wird immer ausgeführt (auch wenn ein Fehler auftritt)  programm wird danach gestoppt der fehler wird aber nicth abgefangen
 #   print("Datei wird geschlossen")


#print("Programmende")
