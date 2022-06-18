for i in range(1,101):
    s = ''
    if (i % 3 == 0):
        s += 'Fizz'
    if (i % 5 == 0):                    #FizzBuzz
        s += 'Buzz'
    if (i % 3 == 0 and i % 5 == 0):
        s += 'FizzBuzz'    
    if not s:
        s += str(i)
    print (s)