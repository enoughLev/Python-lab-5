import sys

word_indices = {}
words = []

index = 0
for line in sys.stdin:
    for word in line.split():
        if word not in word_indices:
            word_indices[word] = index
        words.append(word)
        index += 1

capitalized_words = [(word_indices[w], w) for w in word_indices if w[0].isupper()]

capitalized_words.sort(key=lambda x: x[1])

for idx, w in capitalized_words:
    print(idx, '-', w)

# точки в конце слов, начинающихся с большой буквы не ставим!
