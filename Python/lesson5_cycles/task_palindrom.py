num = int(input("Введите число:"))
temp = num
rev = 0
while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig               #Палиндром (Читается с права налево эдентично)
    num = num // 10
if(temp == rev):
    print("Это палиндром!")
else:
    print("Это не палиндром!")