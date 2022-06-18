words = set()
for _ in range((int(input()))):
    words.update(input().split())           #Колличество строк и слов в тексте
print(len(words))