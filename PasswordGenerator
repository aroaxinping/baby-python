import random

# Available characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Ask user for input
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# Step 1: Create an EMPTY list (like an empty bag)
password_list = []
# ⚠️ WHY? Because we need a place to store our characters!

# Step 2: Add random letters to the list
for letter in range(0, nr_letters):
    random_letter = random.choice(letters)  # Pick a random letter
    password_list.append(random_letter)      # Put it in the bag
    print(f"Added letter: {random_letter}")  # See what we added

# Step 3: Add random numbers to the list
for number in range(0, nr_numbers):
    random_number = random.choice(numbers)
    password_list.append(random_number)
    print(f"Added number: {random_number}")

# Step 4: Add random symbols to the list
for symbol in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)
    print(f"Added symbol: {random_symbol}")

print(f"\nBefore shuffling: {password_list}")

# Step 5: Mix everything randomly (like shaking the bag)
random.shuffle(password_list)
print(f"After shuffling: {password_list}")

# Step 6: Create an EMPTY string (like an empty text box)
password = ""
# ⚠️ WHY? Because we need a place to build our final password!

# Step 7: Convert list to string (take items from bag and write them down)
for character in password_list:
    password += character  # Add each character to our string
    print(f"Building password: {password}")

print(f"\n✅ Your password is: {password}")
