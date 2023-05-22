import random
input("Welcome To DiceRoll Press Enter To Roll")
def diceroll(sides):
    import random
    side1=random.randrange(sides)+1
    return(side1)
die1= diceroll(6)
die2= diceroll(6)
total=die1+die2
print("you rolled a ",total)
if (total==2 ):
    print("You lose")
elif (total==3 ):
    print("You lost")
elif (total==12):
    print("Your Dog Water")  
elif (total==7):
    print("Lets Go Your Amazing")
elif (total==11):
    print("Your So Smart You Won")
else:
    point=total
    print("Your point is ",point)
    input("Hit enter to roll")
    die1=diceroll(6)
    die2=diceroll(6)
    total=die1+die2
    print("you rolled a",total)
    while (total != 7) and(total != point):
        die1=diceroll(6)
        die2=diceroll(6)
        total=die1+die2
        print("you rolled a",total)
        input("Hit Enter To Roll")
    if(total==point):
        print("Yippy You Won")
    else:
        print("LOL Your An Actual Looser")
        






