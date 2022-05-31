import numbers


numbers = int(input('Введите число'))
sum = 0
if numbers < 0: numbers = numbers * -1
while numbers > 0:
 a = numbers % 10
 sum = sum + a
 numbers = numbers // 10
print("Сумма цифр числа равна:", sum)