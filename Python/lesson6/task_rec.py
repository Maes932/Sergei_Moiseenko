def binary_strings(n, balance=3, st=''):     
    if balance < 0:
        return
    if n == 0:
        if balance == 0:                                 #Бинарные числа
            print(st)
        return
    binary_strings(n - 1, balance - 1, st + '1')
    binary_strings(n - 1, balance + 1, st + '0')
    binary_strings(n - 1, balance - 1, st + '0')
    binary_strings(n - 1, balance + 1, st + '1')
binary_strings(3)
print() 
lst = ['жить', 'этим', 'с', 'теперь', 'как']
def print_forward(lst):
    if len(lst) != None:
        print(lst.pop(-1))
        return lst
print_forward(lst)
print_forward(lst)                                 #слова наоборот
print_forward(lst)
print_forward(lst)
print_forward(lst) 
    
    
  print(*data[27:278:1], sep='\n')  
    




