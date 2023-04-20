import sys

print("Введите слово:")
word = input()

score = 0

english_scores = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

russian_scores = [1, 3, 1, 2, 1, 1, 2, 2, 1, 5, 3, 3, 3, 3, 1, 1, 5, 5, 5, 5, 8, 3, 10, 8, 10, 10, 3, 3, 5, 5, 5, 5, 4, 5]

scores = []
if word.isalpha() and all(ord(c) < 128 for c in word): 
    scores = english_scores
elif word.isalpha(): 
    scores = russian_scores
else:
    print("Введено некорректное слово!")
    sys.exit()

for c in word:
    c = c.lower()
    index = ord(c) - ord('a') 
    if scores == russian_scores:
        index = ord(c) - ord('а') 
    if 0 <= index < len(scores): 
        score += scores[index]

print("Стоимость слова", word, ":", score)
