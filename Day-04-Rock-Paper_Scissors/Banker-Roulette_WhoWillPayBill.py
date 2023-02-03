import random

names = input("Enter the names separated by comma: ")
split_name = names.split(',')

num=len(split_name)

random_choice= random.randint(0,num-1)

person = split_name[random_choice]

print(f'{person} wiil be paying')