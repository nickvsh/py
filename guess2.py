print("--------")
print('Welcome')
g = input('\tTry to Guess the number: ')
guess = int(g)
print("--------")
print("You entered ", guess, "")
print("--------")
if guess == 5:
    print("\t*********")
    print("\tYou win!");
    print("\t*********")
else:
    print("\t*********")
    print("\tYou lose");
    print("\t*********")
print("Game over")
