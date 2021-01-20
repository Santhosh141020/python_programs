import random
guess=int(input("Guess a number in range of 1 to 30\n"))
ele=random.randint(0,30)
while True:
    if ele==guess:
        print("You guessed it right\n")
        break
    elif ele>guess:
        guess=int(input("Guess a number higher than this\n"))
    else:
        guess=int(input("Guess a number lower than this\n"))
    
