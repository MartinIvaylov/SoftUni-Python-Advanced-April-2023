from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words_to_find = {"rose": "rose" , "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
found_word = False

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for word in words_to_find.keys():
        words_to_find[word] = words_to_find[word].replace(current_vowel, '')
        words_to_find[word] = words_to_find[word].replace(current_consonant, '')

        if words_to_find[word] == '':
            print(f"Word found: {word}")
            found_word = True
            break
    if found_word:
        break


if not found_word:
    print(f"Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
