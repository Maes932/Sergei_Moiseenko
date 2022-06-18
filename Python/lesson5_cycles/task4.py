a = {}
for _ in range(int(input())):
    s = input().split()
    country, cityes = s[0], s[1:]
    for city in cityes:                  #Города сделал чуть иначе
        a[city] = country
for i in range(int(input())):
    print(a[input()])