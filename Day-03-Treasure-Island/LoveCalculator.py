print("Welcome to Love Calculator")
name1 = input("Enter your name: ")
name2 = input("Enter the other person's name: ")

name1 = name1.lower()
name2 = name2.lower()

combined_string = name1+name2
print(combined_string) 

t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')

true = t+r+u+e

l = combined_string.count('l')
o = combined_string.count('o')
v = combined_string.count('v')
e = combined_string.count('e')

love = l+o+v+e

love_score = true+love

if(love_score > 0 and love_score < 30):
    print(f'Your love score is {love_score}% . You are like water and fire.')
elif(love_score > 30 and love_score < 60):
    print(f'Your love score is {love_score}% . You guys are alright')
else:
    print(f'Your love score is {love_score}% . You are like fish and chips.')
