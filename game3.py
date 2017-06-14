from random import randint
secret_number = randint    (1, 10)

print ("Howdy, stranger")
print("---------")
guess = 0
while guess != secret_number:
    g = input ("Guess the magic number:\t")
    guess = int(g)
    if guess > secret_number:
        print("Too high")
        print("Never give up\nTry again, plz")
    else:
        if guess < secret_number:
            print("Too low")
            print("Never give up\nTry again, plz")
        else:
            print("**************")
            print("Congratulations. You win!")
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
    print("---------")
print("Game over")
print(secret_number)

