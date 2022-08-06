import random
import time
import sys

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
	if comp != 1 and comp % 2 != 0 and comp % 3 != 0 and comp % 5 != 0 and comp % 7 != 0 or comp == 2 or comp == 3 or comp == 5 or comp == 7:
		clueList.append(clues[6])			
	if comp >= 25:
		clueList.append(clues[7])
	if comp <= 25:
		clueList.append(clues[8])
	clueList.append("There are no other clues left.")

	# Introduction of the game - function
	def intro():
		print("Welcome to Number Guessing game !!!")
		print("Instructions:\n")
		print("1. Computer will choose one number between the range 1 to 50.")
		print("2. Using five chances and various clues, you want to guess that number.")
		print("3. For every wrong answers, score will minus by 1.")
		print("4. Please the number within the range 1-50 !\n")
	intro()

	# Play Again Function
	def play_again():
		print("--------------------------------------------------")
		again = input("\n\nDo you want to play again[Y/N]: ").lower()
		if again == 'y':
			main()
		else:
			time.sleep(2)
			sys.exit()

	# Main Loop or Main Algorithm
	def main_func():
		num_clue = 0
		score = 5
		chance = 0
		show_chance = 1

		for i in range(1, 6):
			try:
				human = int(input("Guess the number within range(1-50): "))

				if human >= 1 and human <= 50:
					if human == comp:
						print("You had guessed the number correctly.\n")
						print("Your final score is", score, '.')
						print("You guessed the number with", show_chance, 'chances.')
						time.sleep(1)
						play_again()

					if human != comp:
						print("It was Wrong. \t\t Score =", score - 1)
						chance + 1
						print(clueList[num_clue])
						print("Try Again :(\n")

						# Code to print clues one by one
						if num_clue == 0 or num_clue == 1:
							num_clue += 1
						elif num_clue == 2 or num_clue == 3:
							num_clue = 0
						
				else:
					print("Please type within the range !\n")
				score -= 1
				chance += 1
				show_chance = chance + 1

			except ValueError:
				print("Please type only number !\nexiting")
				time.sleep(1)
				play_again()

		# Printing Final Score

		print("============================================")
		print("|| Correct answer is", comp, ".                 ||")
		print("|| Your final score is", score, ".                ||")
		print("|| You used 5 chances.			  ||")
		print("============================================\n")
		play_again()

	# Printing how many clues and chances

	len_list = len(clueList) - 1
	print("============================================")
	print("|| You have only", len_list, "clues and              ||")
	print("|| 	                                  ||")
	print("|| You have 5 chances.			  ||")
	print("============================================\n")
	main_func()

main()


