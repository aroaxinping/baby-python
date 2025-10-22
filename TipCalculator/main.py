print("Hi! Welcome to the tip calculator! ₍^. .^₎⟆\n")
bill = float(input("- How much was the total bill? "))

tip_input = input("Okay, what percentage tip would you like to give? ")

# Asegurarnos de trabajar con string antes de convertir en float y dividir entre 100
#añadido por mi para que si el usuario añade el simbolo %, no de error
if "%" in tip_input:
    tip_input = tip_input.replace("%", "")

tip = float(tip_input) / 100  # ahora sí convertimos a float

#print(tip)
people = int(input("How many people to split the bill? "))
total = tip * int(bill) / int(people)
#print(total)
total = round(total, 2)

#añadido por mi para que si es un numero redondo, no ponga .0
if total.is_integer():
    total = round(total)

print(f"\nAlright, then each person should pay a {total} € tip!")





