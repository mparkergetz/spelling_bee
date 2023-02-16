
import json
import numpy as np
import random
from collections import Counter

with open('english.txt') as g:
    lines = g.read()
    lines = lines.split('\n')

seven_let_all = []
pangrams = []
for i in lines:
    if (len(set(i)) <= 7) & (len(i) >3):
        seven_let_all.append(i)
    if len(set(i)) == 7:
        pangrams.append(i)

pangram_today = np.random.choice(pangrams)

word_list_today = []
alt_pangrams = []
for i in seven_let_all:
    if set(i).issubset(set(pangram_today)):
        word_list_today.append(i)
        if len(set(i)) == 7:
            alt_pangrams.append(i)

letters_today = list(set(pangram_today))
total_count = len(word_list_today)
words_guessed = 0
words_guessed_list = []
congrats = ['Nice', 'Great', 'Excellent']

while True:
    print(' '.join(letters_today))
    my_input = input("Type your word here: ")
    if words_guessed == total_count:
        break
    elif my_input == 'q':
        ans = input("Quit? y/n ")
        if ans == 'y':
            break
    elif my_input == ' ':
        random.shuffle(letters_today)
        continue
    elif my_input == 'h':
        first_lets = [x[:2] for x in word_list_today]
        first_lets.sort()
        hint = Counter(first_lets)
        for i in hint:
            print(i, hint[i])
        continue

    elif my_input in word_list_today:
        words_guessed += 1
        word_list_today.remove(my_input)
        words_guessed_list.append(my_input)
        if my_input in alt_pangrams:
            print('!!!!PANGRAM!!!!')
        else:
            print(np.random.choice(congrats))
    else:
        print('Not in word list')
    print(('X'*words_guessed),('.'*total_count))
    print(np.sort(words_guessed_list), '\n\n\n')






print("\nToday's pangram:",alt_pangrams)
print("Word list:\n", word_list_today)
