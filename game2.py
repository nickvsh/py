print ("Howdy, stranger")
print("---------")
guess = 0
while guess != 5:
    g = input ("Guess the magic number:\t")
    guess = int (g)
    if guess == 5:
            
            print("***************")
            print("***************")
            print("******* *******")
            print("******   ******")
            print("******   ******")
            print("******   ******")
            print("******   ******")
            print("******   ******")
            print("******   ******")
            print("******   ******")
            print("******   ******")
            print("******   ******")
            print("***************")
            print("***************")
            print("******   ******")
            print("******   ******")
            print("***************")
            print("***************")
            
            print("\nCongratulations. You win!")
            print("***************")
    else:
        if guess < 5:
            print("Too low")
            print("Never give up\nTry again, plz")
        else:
            print("Too high")
            print("Never give up\nTry again, plz")         
    print("---------")
print("Game over")

