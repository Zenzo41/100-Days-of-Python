word_list =['random','rumba','lambda']

import random

chosen_word = random.choice(word_list)

guess =input("Guess a letter of the word: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")