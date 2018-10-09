import random

print ("\tGuess My Number Games")
print ("\nThe range of number is 1 - 10")
print ("And you have 5 chance to guess it")

trie = 1
number = random.randint(1, 10)
guess = int(input("\nGuess the number : "))

while guess != number:
	if guess > number:
		print ("Lower")
    else:
        print ("Higher")

    guess = int(input("Guess the number : "))
    trie += 1
    if trie == 5:
        print ("\nGame Over")
        print ("The number is ", number)
        break

if guess == number:
    print ("\nFinish")
    print ("You guessed the number")
