

def fibonacci():
    fib1 = 0
    fib2 = 1
    rank = 1
    while rank <= 20:
        print(rank, fib2)
        temp = fib2
        fib2 += fib1
        fib1 = temp
        rank+=1
        
    
fibonacci()