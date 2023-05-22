input("Your lone hero is surrounded by a massive army of trolls.\n")
input("Thier decaying green bodies stretch out, menting into the horizon.\n")
input("Your hero unsheathes a sword and begins the ast fight of there life.\n")

health=10
trolls=0
damage=3

input("Hit enter to fight")
while (health >0):
    trolls +=1
    health=health - damage
    print("Your hero swings and defeats and evil troll.")
    print("but takes", damage, "damage points.\n")
    print("but takes-",health)
    input("Hit Enter to fight")

print("your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero is no more.")

input("\n\nPress the enter key to exit.")

