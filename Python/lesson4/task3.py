tup = (1, )
for element in tup:
    element += 1                   #Создание кортежа с одним элементом
    for element_two in tup:
        element_two += 2
    print(tup + (element, ) + (element_two, ))
print('Возращение колличества элементов в кортеже = ', len(tup))  
         
   
  
       
    




