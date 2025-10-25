print("""
    // ""--.._
   ||  (_)  _ "-._
   ||    _ (_)    '-.
   ||   (_)   __..-'
    \\__..--""
""")

print("WELCOME TO PYTHON PIZZA DELIVERIES!\n")

size = input("- What size pizza do you want? S, M or L: ")
bill = 0

if size == "S" or size == "s":
    bill = 15
    print("okay, size s pizzas are 15$\n")

elif size == "M" or size == "m":
    bill = 20
    print("okay, size m pizzas are 20$\n")

elif size == "L" or size =="l":
        bill = 25
        print("okay, size l pizzas are 25$\n")

else:
    print("sorry, I didn't quite understand you, you typed the wrong inputs")

pepperoni = input("- Would you like some pepperoni on your pizza? Y or N: ")
if pepperoni == "Y" or pepperoni =="y":
    if size == "S" or size =="s":
        bill += 2
    elif size == "M" or size =="m":
        bill += 3
    elif size == "L" or size=="l":
        bill += 3
elif pepperoni == "N" or pepperoni=="n":
    bill += 0

print(f" With pepperoni, your pizza will be {bill} $, \n")

extracheese = input("- Do you also want extra cheese for just 1$ ? Y or N: ")
if extracheese == "Y" or extracheese=="y":
    bill += 1
elif extracheese == "N" or extracheese=="n":
    bill += 0

print(f"Alright! that will be {bill} $ in total, enjoy your meal!")




