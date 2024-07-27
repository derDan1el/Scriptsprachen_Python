


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