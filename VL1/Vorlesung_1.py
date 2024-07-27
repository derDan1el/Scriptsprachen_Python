for x in [1,2,3,4,5]:
    print(str(x) + " " + str(x**2))
    print(f"{x} {x**2}")
print("---------------------------------")

print("Oktalzahlen werden mit 0o und dann die zahl zb 0o22 ="+str(0o22))

print("binärzahlen werden mit 0b und dann die zahl zb 0b1010 ="+str(0b1010))

print("hexadezimalzahlen werden mit 0x und dann die zahl zb 0x22 ="+str(0x22))

print("---------------------------------")


print(f"was ergibt 0.1 + 0.2 xD : {0.1 +0.2}")

print(f"der typ von variablen kann mit type(zahl) zb rausgefundne werden : {type(0.1)}")

print(f" 3.0/2 ergibt : {3.0/2} wohingegen 3/2 ergibt auch : {3/2}aber 3//2 ergibt : {3//2}")


print(f"es gibt none typs wird durch None dargestellt")

print("---------------------------------")
a = None


print(f"der typ von a ist : {type(a)}")

print("---------------------------------")

print(f"es gibt auch listen zb x = [1,2,3,4,5] und elemente hinzufügen geht durch x = x +[20]")

x = [1,2,3,4,5]
print(x)
x = x + [20]
print(x)
print("der liste ist ein veränderbarer datentyp und es wird keine neuer liste erstellt sondern die alte wird verändert")
print("---------------------------------")

print("Es gibt auch strings welche aber unveränderlich sind das heißt es wird eine  neue speicheradresse erstellt und der string wird dort gespeichert")

y= 'hallo'
print(y)
print(id(y))
y = y + ' welt'
print(y)
print(id(y))
print("wenn man schnell und oft unveränderliche datentypen ändert läuft der speicher voll und es wird langsam")

print("---------------------------------")

print("es gibt auch tupel welche unveränderlich sind und mit runden klammern erstellt werden erstellt werden")

t = "hi"

a = ("moin",3,t,True,3.14)
print(a)

print("---------------------------------")
print("listen werden mit eckigen klammern erstellt")

b = [1,2,a,"b","c","d"]
print(b)

print("---------------------------------")
print("man kann strings entweder mit '' oder mit \"\" erstellen solange man die gleichen zeichen benutzt")

print("---------------------------------")

print("hat man eine liste und man möchte sie von hinten durchgehen nutzt man minuszahlen zb x[-1]")

for g in b:
    print(g)

z = b[-1]
print("mit minus ist es")
print(z)

print("---------------------------------")  

print("weitere befehle sind zb b[1:3] gibt element 1 und 2 aus exlusive 3 also 1 und 2")


print(b[1:3])

print("---------------------------------")

print("x in s gibt true oder false zurück ob x in s ist")

print(3 in b)

print ("---------------------------------")

print("x not in s gibt true oder false zurück ob x nicht in s ist")

print(3 not in b)

print ("---------------------------------")

print("'Hallo' * n n kopien von s") 

print("Hallo "*2)


print ("---------------------------------")

print("len(s) gibt die länge von s zurück")

print(len(b))

print ("---------------------------------")

print("min(s) gibt das kleinste element von s zurück")


print("max(s) gibt das größte element von s zurück")

print ("---------------------------------")

print("s.index(x) gibt den index von x in s zurück")

print(b.index(1))

print ("---------------------------------")

print("s.count(x) gibt die anzahl von x in s zurück")

print(b.count(3))

print ("---------------------------------")

print("s.append(x) fügt x am ende von s hinzu")

b.append(3)
print(b)

print ("---------------------------------")

print("s.insert(i,x) fügt x an der stelle i in s ein")

b.insert(2,3)

print(b)

print ("---------------------------------")


