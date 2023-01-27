print(''' 
      
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************''')
print()
print("Welcome to Treasure Island!!")
print("Your mission is to find the treasure.")

left_or_right = input('''You're at a cross road. Where do you want to go? Type "left" or "right" : ''')

if((left_or_right=='left') or (left_or_right=='LEFT')):
    wait_or_swim = input('''You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.''')
    
    if((wait_or_swim=='wait') or (wait_or_swim=='WAIT')):
        red_blue_yellow_door = input('''You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ''')
        
        if((red_blue_yellow_door=='yellow') or (red_blue_yellow_door=='YELLOW') ):
            print("Congrats!! You reached the room with the treasure inside. ")
            
        else:
            print("The room is filled with poisonous gas. You died.")
            
    else:
        print("You were chased and eaten by the lake monster. You died.")
        
else:
    print("This road leads to the Terror Jungle. You didnt survive. You died.")
