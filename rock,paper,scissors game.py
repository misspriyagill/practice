import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]
game = random.choice(list)

print("welcome to the virtual game of rock, paper and scissors")
user_choice = input("what do u want to choose.type 0 for rock, 1 for paper, 2 for scissors.")

computer_choice = random.randint(0, 2)

if user_choice == "0":
    print(f"you chose rock.{rock}")
elif user_choice == "1":
    print(f"you chose paper.{paper}")
elif user_choice == "2":
    print(f"you chose scissors.{scissors}")
else:
    print("please try again with a correct value.")
    quit()

if computer_choice == 0:
    print(f"computer chose rock.{rock}")
if computer_choice == 1:
    print(f"computer chose paper.{paper}")
if computer_choice == 2:
    print(f"computer chose scissors.{scissors}")

if int(user_choice) == int(computer_choice):
    print("its a tie.")
if user_choice == "0" and computer_choice == 1:
    print("Oops looks like You lost, the computer wins.")
if user_choice == "0" and computer_choice == 3:
    print("hurray! the computer loses you are the winner!")
if user_choice == "1" and computer_choice == 0:
    print("hurray! the computer loses you are the winner!")
if user_choice == "2" and computer_choice == 1:
    print("hurray! the computer loses you are the winner!")
if user_choice == "1" and computer_choice == 2:
    print("Oops looks like You lost, the computer wins.")
if user_choice == "2" and computer_choice == 0:
    print("Oops looks like You lost, the computer wins.")
