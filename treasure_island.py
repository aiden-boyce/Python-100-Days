# Day Three
print(
    '''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
      '''
)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("You're at a crossroad. Would you like to go left or right?\n").lower()

if not choice == "left":
    print("You fell into a hole. Game over.")
    exit()

choice = input(
    "You've come to a lake. There's an island in the middle. Wait for a boat or swim?\n"
).lower()

if not choice == "wait":
    print("You were attacked by a trout. Game over.")
    exit()

choice = input(
    "You arrive at the island. There is a house with 3 doors. Will you go through the red, blue, or yellow door?\n"
).lower()

if choice == "yellow":
    print("You win! Yippee!")
elif choice == "red":
    print("You are burned to death. Game over.")
elif choice == "blue":
    print("You are eaten by beasts. Game over.")
else:
    print("Game over.")
