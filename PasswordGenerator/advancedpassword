import random
import string

# Use Python's built-in string module (more elegant)
letters = list(string.ascii_letters)  # All uppercase + lowercase
numbers = list(string.digits)          # 0-9
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# List comprehension (advanced one-liner loops)
password_list = (
    [random.choice(letters) for _ in range(nr_letters)] +
    [random.choice(numbers) for _ in range(nr_numbers)] +
    [random.choice(symbols) for _ in range(nr_symbols)]
)

# Shuffle and convert to string in fewer lines
random.shuffle(password_list)
password = ''.join(password_list)  # Most efficient way to combine strings

print(f"Your password is: {password}")
