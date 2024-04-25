# new_list = map(function, data)
from random import shuffle
words = ['beetroot', 'asd', 'rwer']
anagrams = []

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

# METHOD 1
# for word in words:
#     anagrams.append(jumble(word))

# print(anagrams)

# METHOD 2
print(list(map(jumble, words)))


# METHOD 3
print([jumble(word) for word in words])