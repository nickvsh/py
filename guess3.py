

from random import randint
secret = randint(1,10)

print("Hello");
guess = 0
while guess != secret:
	g = input("Try to guess number:")
	guess = int(g)
	if guess == secret:
		print("You win. Congratulations")
	else:
		if guess > secret:
			print("Too high")
		else:
			print("Too low")
		print("Try again, plz")
print("Game over. Thnks")
