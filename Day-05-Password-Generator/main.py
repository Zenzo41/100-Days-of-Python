#Password Generator Project
import random
import string
lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_characters = ['=','~','!','@','#','$','%','^','&','*','(',')','_','+']
print ("Welcome to the PyPassword Generator!")
lwrcase = int(input("How many lowercase alphabet do you want in your password: "))
upprcase = int(input("How many uppercase alphabet do you want in your password: "))
num = int(input("How many numbers do you want in your password: "))
spcl_char = int(input("How many special characters do you want in your password: "))

# Easy Way
# password = ''
# for char in range(1,lwrcase + 1):
#     randomlwr = random.choice(lowercase_alphabet)
#     password += randomlwr
    
# for char in range(1,spcl_char + 1):
#     randomspcl = random.choice(special_characters)
#     password += randomspcl
    
       
# for char in range(1,upprcase + 1):
#     randomuppr = random.choice(uppercase_alphabet)
#     password += randomuppr
    
    
# for char in range(1,num + 1):
#     randomnum = random.choice(numbers)
#     password += randomnum
    
# print(password)   

#HARD LEVEL
password_list = []
for char in range(1,lwrcase + 1):
    randomlwr = random.choice(lowercase_alphabet)
    password_list.append(randomlwr) 
    
for char in range(1,spcl_char + 1):
    randomspcl = random.choice(special_characters)
    password_list += randomspcl
    
       
for char in range(1,upprcase + 1):
    randomuppr = random.choice(uppercase_alphabet)
    password_list += randomuppr
    
    
for char in range(1,num + 1):
    randomnum = random.choice(numbers)
    password_list += randomnum
    
print("Before Shuffle",password_list)
random.shuffle(password_list)
print("After Shuffle",password_list) 

password= ''
for char in password_list:
    password +=char
    
    
print(f'Your password is: {password}')