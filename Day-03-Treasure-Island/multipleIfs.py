print("Welcome to the RollerCoaster Ride!")
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride it. Just grab a ticket from the counter.")
    
else:
    age = int(input("Enter your age: "))
    if(age >= 18):
        print("You can ride it. Just grab a ticket from the counter.")
    else:
        print("You are too young for this.")
        
photo_or_not = input("Do you wanna take a photo? If yes, Enter Y or y: ")
if(photo_or_not == 'Y' or photo_or_not == 'y'):
    print("Your picture in the rollercoaster has been taken. It looks great")
else:
    print("Are you sure you don't wanna miss your photo? Enjoy the ride too.")