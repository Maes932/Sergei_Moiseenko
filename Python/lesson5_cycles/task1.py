while True:
    num = int(input(' :'))
    fib = [0, 1]
    while len(fib) <= num:                #Фибоначчи 
        fib.append(fib[-2]+fib[-1])
    print(fib[-1])