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
        
