word_set = {}
word_set = set()
N = int(input())

for i in range(N):
    word = input()
    word_set.add(word)

word_set = list(word_set)
word_set.sort()
word_set.sort(key = len)

for i in range(len(word_set)):
    print(word_set[i])