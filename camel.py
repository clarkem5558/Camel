import random

print ("Welcome to Camel!")
print ("You have stolen a camel to make your way across the great Mobi desert.")
print ("The natives want their camel back and are chasing you down! Survive your")
print ("desert trek and out run the natives.")
done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_traveled = -20
canteen_drinks = 100
oasis = 5

while(done == False):
	print ("A. Drink from your canteen.")
	print ("B. Ahead moderate speed.")
	print ("C. Ahead full speed.")
	print ("D. Stop for the night.")
	print ("E. Status check.")
	print ("Q. Quit.")
	user_choice = input("Your Choice? ")
	if user_choice.upper() == 'Q':
		done = True
	elif user_choice.upper() == 'E':
		print ("Miles Traveled", miles_traveled)
		print ("Drinks in Canteen", canteen_drinks) 
		print ("The natives are", natives_traveled, "miles behind you.")
	elif user_choice.upper() == 'D':
		camel_tiredness = 0
		natives_traveled = natives_traveled + 10
		print ("Camel is happy")
	elif user_choice.upper() == 'C':
		miles_traveled = miles_traveled + 20
		thirst = thirst + 1
		camel_tiredness = camel_tiredness + 3
		natives_traveled = natives_traveled + 10
		print ("You have travelled ", miles_traveled)
	elif user_choice.upper() == 'B':
		miles_traveled = miles_traveled + 12
		thirst = thirst + 1
		camel_tiredness = camel_tiredness + 1
		natives_traveled = natives_traveled + 6
		print ("You have travelled ", miles_traveled)
	elif user_choice.upper() == 'A':
		if canteen_drinks > 0:
			canteen_drinks = canteen_drinks - 1
			thirst = 0
			print ("You are no longer thirsty")
		else:
			print ("You have no more water.")
	if (thirst > 4 and thirst <=6):
		print ("You are thirsty!")
	elif thirst > 6:
		print ("You died of thirst")
		done = True
	if (camel_tiredness > 5 and camel_tiredness <= 8):
		print ("Your camel is getting tired")
	elif camel_tiredness > 8:
		if done == False:
			print ("Your camel is dead")
			done = True
	if natives_traveled >= miles_traveled:
		print ("Natives have caught you")
		done = True
	elif miles_traveled - natives_traveled < 15:
		print ("The natives are getting close")
	if miles_traveled >= 200:
		if done == False:
			print ("You've won the game")
			done = True
	oasis_random = random.randrange(1,21)
	if oasis == oasis_random:
		thirst = 0
		camel_tiredness = 0
		canteen_drinks = 100
		print("You found the oasis")
		
		







