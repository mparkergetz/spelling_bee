
import json
import numpy as np
import random
from collections import Counter
from termcolor import colored
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# f = open('words_dictionary.json')
# words = json.load(f)

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
letters_today = list(set(pangram_today))
key_letter = np.random.choice(letters_today)

word_list_today = []
alt_pangrams = []
for i in seven_let_all:
    if (set(i).issubset(set(pangram_today))) & (key_letter in i):
        word_list_today.append(i)
        if len(set(i)) == 7:
            alt_pangrams.append(i)


letters_today.remove(key_letter)


total_count = len(word_list_today)
words_guessed = 0
words_guessed_list = []
congrats = ['Nice', 'Great', 'Excellent']

print(
    '\n\n\n#### Spelling Bee ##################################\n'
    '#### How to play: ##################################\n'
    '####   Use the letters provided to spell ###########\n'
    '####   common English words (many words  ###########\n'
    '####   not included). Each word must     ###########\n'
    '####   contain the first letter in red,  ###########\n'
    '####   and must be at least 4 letters.   ###########\n'
    '####   A Pangram uses each letter at     ###########\n'
    '####   least once. Enter a single space  ###########\n'
    '####   (" ") to shuffle the letters, or  ###########\n'
    '####   "h" for a list of hints, or "q"   ###########\n'
    '####   to quit and reveal the answers.   ###########\n'
    '####################################################\n'
)



while True:
    print(colored(key_letter,'red'),' '.join(letters_today))
    my_input = input("Type your word here: ")
    if words_guessed == total_count:
        break
    elif my_input == 'q':
        ans = input("Quit? y/n ")
        if ans == 'y':
            break
    elif my_input == ' ':
        random.shuffle(letters_today)
        clear()
        continue
    elif my_input == 'h':
        first_lets = [x[:2] for x in word_list_today]
        first_lets.sort()
        hint = Counter(first_lets)
        for i in hint:
            print(i, hint[i])
        print('\n\n\n')
        continue

    elif my_input in word_list_today:
        words_guessed += 1
        word_list_today.remove(my_input)
        words_guessed_list.append(my_input)
        if my_input in alt_pangrams:
            print('/n/n/n!!!!PANGRAM!!!!')
        else:
            print(np.random.choice('/n/n/n/',congrats))
    else:
        print('Not in word list')
    print(('X'*words_guessed),('.'*total_count))
    print(np.sort(words_guessed_list), '\n\n\n')






print("\nToday's pangrams:",alt_pangrams)
print("Word list:\n", word_list_today)