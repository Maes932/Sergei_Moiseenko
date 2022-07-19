with open('E:\\Users\\Сергей\\Desktop\\ratings.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]
print(*data[27:278:1], sep='\n')



