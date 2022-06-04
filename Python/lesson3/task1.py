text = input('Ввод текста-')
letter_lower = 0
letter_upp = 0
for i in text:
    if 'a' <= i <= 'z':
        letter_lower += 1
    else:
        if 'A' <= i <= 'Z':
            letter_upp += 1
print('Количество прописных букв:' ,letter_upp)           
print('Количество строчных букв:', letter_lower)





