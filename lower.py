import random
WORDS=("python","jumble","easy")
word=random.choice(WORDS)
correct=word
jumble=""
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[position]+word[(position+1):]
print ("the jumble is:",jumble)
guess=input("\nyour guess:")
count=1
guess=guess.lower()
while (guess!=correct) and (guess != ""):
    print ("sorry, that's not it.")
    guess=input("\nYour guess:")
    count+=1
    guess=guess.lower()
if guess== correct:
    print ("that's it!")
    print("It took you",count,"guesses")
