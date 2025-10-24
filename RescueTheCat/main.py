print(r'''
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)
''')
print("Welcome to RESCUE THE CAT!")
print("Your mission is to find and save the missing cat.\n")

q1 = input("You're on a cross road. Where do you want to go? Type left or right. ")
if q1 == "left":
    q2 = input("You've come to a lake. There is an island in the middle of the lake.Type wait to wait for a boat or swim to swim across.")

    if q2 == "wait":
        finalq = input("You have arrived at the island unharmed.\nThere is a house with 3 doors. One red, one yellow and one blue. Wich colour do you choose?")

        if finalq == "blue" or finalq == "red":
            print("GAME OVER, YOU DIED.")
        elif finalq == "yellow":
            print("Congratulations! You saved the cat!")

    if q2 == "swim":
        print("GAME OVER, YOU DROWNED.")

if q1 == "right":
    print("GAME OVER, YOU GOT LOST.")
else:
    print("invaldi choice")