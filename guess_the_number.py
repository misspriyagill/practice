logo="""   _   _   _   _   _     _   _   _     _   _   _   _   _   _  
  / \ / \ / \ / \ / \   / \ / \ / \   / \ / \ / \ / \ / \ / \ 
 ( g | u | e | s | s ) ( t | h | e ) ( n | u | m | b | e | r )
  \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ 
  """
from random import randint


easy_level_turns = 10
hard_level_turns = 5
super_hard_level_turns = 5


def set_difficulty(user_choice):
    if user_choice=="easy":
        return easy_level_turns
    elif user_choice=="hard":
        return hard_level_turns
    elif user_choice=="super hard":
        return super_hard_level_turns
    else:
        print("Type a valid answer!")

def check_answer(guess,answer,turns,difficulty):
    if guess==answer:
        print(f"You got it!The answer is {answer}")
    elif (abs(guess-answer)<=5) and (difficulty=="easy" or difficulty=="hard"):
        print("You are almost there!")
        return turns-1
    elif (abs(guess-answer)<10) and (difficulty=="easy" or difficulty=="hard"):
        print("You are close,but not quite there!")
        return turns-1
    elif guess>answer and (difficulty=="easy" or difficulty=="hard"):
        print("too high!")
        return turns-1
    elif guess<answer and (difficulty=="easy" or difficulty=="hard"):
        print("too low!")
        return turns-1
    elif guess!=answer and difficulty=="super hard":
        print("nope.guess again")
        return turns-1
    else:
        print("smthg wrong")

def game():
    print(logo)
    print("Welcome to a number guessing game!")
    print("I'm thinking of a number between 1 to 100.....")
    user_choice = input("Choose a difficulty.\nType 'easy' or 'hard' or 'super hard': ").lower()
    answer=randint(1,100)
    #print(answer)
    turns=set_difficulty(user_choice)
    guess=0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns, user_choice)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()