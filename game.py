print("Welcome, bro")
g = input("Guess the number:\t")
guess = int(g)
if guess == 5:
    print("You win :-)")
else:
    print("You lose :-(")
    if guess > 5:
        print("Too high")
    else:
        print("Too low")
print("---------\nGame over!\n---------")
