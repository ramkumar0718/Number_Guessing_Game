import random
import sys
import time

def main():
	comp = random.randint(1, 50)

	clueList = []
	clues = ["Clue = it is neither prime nor composite number.",
			 "Clue = it is multiple of 2.",
			 "Clue = it is multiple of 3.",
			 "Clue = it is multiple of 4.",
			 "Clue = it is multiple of 5.",
			 "Clue = it is multiple of 7.",
			 "Clue = it is prime number.",
			 "Clue = it is greater than or equal to 25.",
			 "Clue = it is lesser than or equal to 25."]

	# Listing Clues
	if comp == 1:
		clueList.append(clues[0])
	if comp % 2 == 0:
		clueList.append(clues[1])
	if comp % 3 == 0:
		clueList.append(clues[2])
	if comp % 4 == 0:
		clueList.append(clues[3])
	if comp % 5 == 0:
		clueList.append(clues[4])
	if comp % 7 == 0:
		clueList.append(clues[5])
	if comp != 1 and comp % 2 != 0 and comp % 3 != 0 and comp % 5 != 0 and comp % 7 != 0:
		clueList.append(clues[6])			
	if comp >= 25:
		clueList.append(clues[7])
	if comp <= 25:
		clueList.append(clues[8])
	clueList.append("There are no other clues left.\n")

	# Introduction of the game
	def intro():
		print("Welcome to Number Guessing game !!!")
		print("Instructions:\n")
		print("1. Computer will choose one number between the range 1 to 50.")
		print("2. Using various clues, you want guess that number.")
		print("3. You can see below how many clues and chances are there.")
		print("4. For every wrong answers, score will minus by 1.")
		print("5. You can see clue by, typing a number at first.")
		print("6. You want to type the number within the range(1-50).\n")
	intro()

	# Printing how many clues.
	len_list = len(clueList) - 1
	print("You have only", len_list , "clues and")

	# Main Loop
	def main_func(y):
		x = 1
		score = 12
		c = 0
		chance = 1
		while x < y:				
			for i in range(len_list):
				human = int(input("Guess the number within range(1-50): "))
				if human == comp:
					print("You had guessed the number correctly.\n")
					print("Your final score is", score, '.')
					print("You guessed the number with", chance, 'chances.')
					time.sleep(6)
					sys.exit()

				if human >= 1 and human <= 50:
					if human != comp:
						print("It was Wrong. \t\t Score =", score - 1)
						c + 1
						print(clueList[i])
						print("Try Again :(\n")
				else:
					print("Please type within the range !")
				score = score - 1
				c = c + 1 
				chance = c + 1

			print("There are no other clues left.\n")	
			if x == y:
				break
			x = x + 1

		print("Correct answer is", comp, '.')
		print("Your final score is", score, '.')
		print("You used 12 chances.")
		print("--------------------------------------------------")

		again = input("\n\nDo you want to play again[y/n]: ").lower()
		if again == 'y':
			main()
		else:
			time.sleep(2)
			sys.exit()

	# Printing how many chances
	if len_list == 2:
		print("You have 12 chances.\n")
		main_func(6.1)
	if len_list == 3:
		print("You have 12 chances.\n")
		main_func(4.1)
	if len_list == 4:
		print("You have 12 chances.\n")
		main_func(4)

main()

