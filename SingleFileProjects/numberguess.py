import random
import math

print("Guess my number. (*Hint: it's less than 1000 and also positive)")
num = random.randint(0,1000)
i = 1
userIn = -1
maxGuessesAllowed = math.ceil(math.log(1000,2))
while userIn !=num and i<maxGuessesAllowed:
    userIn =  int(input("Enter guess #{}: ".format(i)))
    if userIn>num:
        print("I'm thinking lower.  ", end=" ")
    elif userIn<num:
        print("I'm thinking higher. ", end=" ")
    i+=1
   

if userIn == num:
    print(f"\nNice! You guessed it in {i-1} tries. You had {maxGuessesAllowed - (i-1)} guesses left. Good job!")
else:
    print("\n\nWell... you failed, and at the simplest game known to mankind.")
    print("You should take a moment for deep introspection and reflect on your life choices.")
    print("Perhaps one day, you'll find enlightenment... but today is not that day.")
    

            





