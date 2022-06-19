lst = ['xy', 'xz', 'xv', 'yy', 'yz', 'yv']
a = [x for x in lst]
print(a[::2])                                #Использование слайса в генераторе!
lst_1 = ['1x', '2x', '3x', '4x']          # Удаление и добавление элемента в генератор!
a = [x for x in lst_1]
a.pop(1)
b = a.copy()
c = [x for x in b]
c.insert(1, '2x')
print(b)