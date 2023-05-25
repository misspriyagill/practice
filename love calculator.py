print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()
combined_string = lowercase_name1 + lowercase_name2

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
true = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")
love = l + o + v + e

love_score = str(true) + str(love)
result = int(love_score)
if result < 10 or result > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif result < 50 and result > 40:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")
