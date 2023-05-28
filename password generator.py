import random,string   #imported string library to replace the lists

# Removed The Lists containing the letters, digits and special symbols

print("Welcome to the Password Generator!")
nr_letters= int(input("\nHow many letters would you like in your password?\n"))
nr_symbols = int(input("\nHow many symbols would you like?\n"))
nr_numbers = int(input("\nHow many numbers would you like?\n"))

password=str()  # changed to type casting for clearer picture

for i in range(1,nr_letters+1):
  random_letter=random.choice(string.ascii_letters)
  password+=random_letter
  
for i in range(1,nr_symbols+1):
  random_symbol=random.choice(string.punctuation)
  password+=random_symbol
  
for i in range(1,nr_numbers+1):
  random_number=random.choice(string.digits)
  password+=random_number

# Replaced the extra list comprehensions  with random.sample to directly shuffle the password string  
result = ''.join(random.sample(password, len(password)))
print("\nYour password is :", result)
