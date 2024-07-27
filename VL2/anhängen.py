

def append_(a = 1, liste = None):
    if liste is None:
        liste = []
    liste += [a]
    return liste


print(append_(1))

print(type(append_))
print(type(12.2345345345345))


def geldbetrag():
    geld = input("Wie viel Geld hast du? ")
    try:
        geld = float(geld)
        if(geld < 0):
            print(" du hast anscheinened Schulden")
            return geldbetrag()
        else:
            hunderter = geld //100
            fünfziger = geld // 50
            zehner = geld // 10
            fünfer = geld // 5
            zweier = geld // 2
    except ValueError:
        print("Das war keine Zahl")
        return geldbetrag()


print('a' == 'A')
print('a' == 'a ')
print('Python' == 1)
print(123 > 2)
print('123' > '2')
print('Monty' != 'Monty')
print(12.2 > 12)
print(3 > 4 + 12)
print((3 > 4) + 12)
print('adenin' in 'Trisulfatmonoadeninpentose')
print(19 not in (5, 19, 36, 69, 119, 149))
print([1,2,3] is [1,2,3])
print(not (True or not False and not True) or False and not True or not False)
print(4 > (9-(1+1)**2))
print((not 'e' > 'bc') and ('a' <= 5))
print(len([(1, 2), ([True], [False, True])]) > len((1,2,True,False,True)))
print([[]] != False and not '' == True)
print(len([(1, 2), ([True], [False, True])]))
print(('a' <= 5) and (not 'e' > 'bc'))