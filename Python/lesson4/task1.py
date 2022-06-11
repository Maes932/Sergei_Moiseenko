from statistics import median


meaning = list(map(int, input().split()))
meaning.sort()
least = meaning[-1]
meaning.sort()
greatest = meaning[0]                 
med = median(meaning)
print('Минимальное число в списке - ', greatest)
print('Медиана числа в списке - ', med)
print('Максимальное число в списке - ', least)
#Поиск минимального,максимального числа и медианы списка
