import random
from game_art import logo,vs
from game_data import data
from replit import clear

def get_random_account():
    account=random.choice(data)
    return account

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# account=get_random_account()
# now=format_data(account)
# print(now)

def check_answer(guess,a_followers,b_followers):
    if a_followers>b_followers and guess=="a":
        return "True"
    elif a_followers>b_followers and guess=="b":
        return "False"
    else:
        print("Enter a valid guess!!!")


def game():
    print(logo)
    score=0
    account_a=get_random_account()
    account_b=get_random_account()
    continue_game =True

    while continue_game:
        account_a=account_b
        account_b=get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"\n Compare A: {format_data(account_a)}\n")
        print(vs)
        print(f"\n Compare B: {format_data(account_b)}\n")

        guess=input("\n Who has more followers on instagram? Type 'A' or 'B'.\n").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_right=check_answer(guess,a_follower_count,b_follower_count)

        clear()
        print(logo)

        if is_right:
            score+=1
            print(f"\nYou are right! current score: {score}\n")
        elif is_right==False:
            continue_game=False
            print(f"\nYou are wrong! final score: {score}\n")
        else:
            continue_game==False
            print(f"Enter a valid guess!!!")

game()

