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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1=input("you are alone and scared in the dark forest.You hear a strange man approach you, he asks you to come along with him to the left saying he can lead you to the treasure. where do u want to go left or right?").lower()

if choice1 =="left":
    choice2=input("you see a lake. the strange man asks if you want to wait for his friend's boat or swim across.do you want to wait or swim?").lower()
elif choice1=="right":
    print("the strange man leaves.you find yourself lost in the forest,unfortunately you become a lion's snack.GAME OVER!")
    quit()
else:
    print("please try again.")
    quit()

if choice2 =="wait":
   choice3=input("you have reached the shore unharmed.you see three brightly coloured doors,first one is red, second one is yellow and the third one is blue.the strange man says that the treasure is behind one of the doors. which door do you want to choose red, yellow or blue?").lower()
elif choice2=="swim":
    print("you get eaten by the crocodiles.GAME OVER!")
    quit()
else:
    print("please try again.")
    quit()

if choice3=="yellow":
    print("congratulations. you have reached the final treasure. YOU WIN!")
elif choice3=="red" or "blue":
    print("the room is filled with flames. you get burned alive.GAME OVER!")
else:
    print("please choose an appropriate answer and try again.")