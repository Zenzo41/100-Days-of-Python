import random

word_list = ["antelope", "capybara", "penguin"]
chosen_word = random.choice(word_list)


# list to append the blank space for total no of letter 
display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display.append("_")
    
print("The word is :",display)

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        
print(display)