import os

def two(pickaxes,pickaxe,inventory,money,enchantments,quests):
	os.system("clear")
	print("What to sell?")
	print("0. Sell All")
	pickaxechecker = sum(len(l) for l in pickaxes)
	if pickaxechecker == 2:
		print("1. Stone")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[0][1],"stone")
			howmany = input("How much stone? ")
			if int(howmany) > int(inventory[0][1]):
				print("Not enough stone!!!")
			else:
				inventory[0][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[0][1] * 1)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[0][1] -= inventory[0][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	if pickaxechecker == 4:
		print("1. Stone")
		print("2. Coal")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[0][1],"stone")
			howmany = input("How much stone? ")
			if int(howmany) > int(inventory[0][1]):
				print("Not enough stone!!!")
			else:
				inventory[0][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[1][1],"coal")
			howmany = input("How much coal? ")
			if int(howmany) > int(inventory[1][1]):
				print("Not enough coal!!!")
			else:
				inventory[1][1] -= int(howmany)
				moneygained = int(howmany) * 2
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[0][1] * 1) + (inventory[1][1] * 2)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[0][1] -= inventory[0][1]
			inventory[1][1] -= inventory[1][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	if pickaxechecker == 6:
		print("1. Stone")
		print("2. Coal")
		print("3. Chain")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[0][1],"stone")
			howmany = input("How much stone? ")
			if int(howmany) > int(inventory[0][1]):
				print("Not enough stone!!!")
			else:
				inventory[0][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[1][1],"coal")
			howmany = input("How much coal? ")
			if int(howmany) > int(inventory[1][1]):
				print("Not enough coal!!!")
			else:
				inventory[1][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[2][1],"chain")
			howmany = input("How much chain? ")
			if int(howmany) > int(inventory[2][1]):
				print("Not enough chain!")
			else:
				inventory[2][1] -= int(howmany)
				moneygained = int(howmany) * 5
				money += moneygained
				print("You got $"+ str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[0][1] * 1) + (inventory[1][1] * 2) + (inventory[2][1] * 5)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[0][1] -= inventory[0][1]
			inventory[1][1] -= inventory[1][1]
			inventory[2][1] -= inventory[2][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	if pickaxechecker == 8:
		print("1. Stone")
		print("2. Coal")
		print("3. Chain")
		print("4. Brick")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[0][1],"stone")
			howmany = input("How much stone? ")
			if int(howmany) > int(inventory[0][1]):
				print("Not enough stone!!!")
			else:
				inventory[0][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[1][1],"coal")
			howmany = input("How much coal? ")
			if int(howmany) > int(inventory[1][1]):
				print("Not enough coal!!!")
			else:
				inventory[1][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[2][1],"chain")
			howmany = input("How much chain? ")
			if int(howmany) > int(inventory[2][1]):
				print("Not enough chain!")
			else:
				inventory[2][1] -= int(howmany)
				moneygained = int(howmany) * 5
				money += moneygained
				print("You got $"+ str(moneygained))
		elif sellchoice == "4":
			os.system("clear")
			print("You have",inventory[3][1],"brick")
			howmany = input("How much brick? ")
			if int(howmany) > int(inventory[3][1]):
				print("Not enough brick!")
			else:
				inventory[3][1] -= int(howmany)
				moneygained = int(howmany) * 7
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[0][1] * 1) + (inventory[1][1] * 2) + (inventory[2][1] * 5) + (inventory[3][1] * 7)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[0][1] -= inventory[0][1]
			inventory[1][1] -= inventory[1][1]
			inventory[2][1] -= inventory[2][1]
			inventory[3][1] -= inventory[3][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	if pickaxechecker == 10:
		print("1. Stone")
		print("2. Coal")
		print("3. Chain")
		print("4. Brick")
		print("5. Iron")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[0][1],"stone")
			howmany = input("How much stone? ")
			if int(howmany) > int(inventory[0][1]):
				print("Not enough stone!!!")
			else:
				inventory[0][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[1][1],"coal")
			howmany = input("How much coal? ")
			if int(howmany) > int(inventory[1][1]):
				print("Not enough coal!!!")
			else:
				inventory[1][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[2][1],"chain")
			howmany = input("How much chain? ")
			if int(howmany) > int(inventory[2][1]):
				print("Not enough chain!")
			else:
				inventory[2][1] -= int(howmany)
				moneygained = int(howmany) * 5
				money += moneygained
				print("You got $"+ str(moneygained))
		elif sellchoice == "4":
			os.system("clear")
			print("You have",inventory[3][1],"brick")
			howmany = input("How much brick? ")
			if int(howmany) > int(inventory[3][1]):
				print("Not enough brick!")
			else:
				inventory[3][1] -= int(howmany)
				moneygained = int(howmany) * 7
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "5":
			os.system("clear")
			print("You have",inventory[4][1],"iron")
			howmany = input("How much iron? ")
			if int(howmany) > int(inventory[4][1]):
				print("Not enough iron!")
			else:
				inventory[4][1] -= int(howmany)
				moneygained = int(howmany) * 10
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[0][1] * 1) + (inventory[1][1] * 2) + (inventory[2][1] * 5) + (inventory[3][1] * 7) + (inventory[4][1] * 10)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[0][1] -= inventory[0][1]
			inventory[1][1] -= inventory[1][1]
			inventory[2][1] -= inventory[2][1]
			inventory[3][1] -= inventory[3][1]
			inventory[4][1] -= inventory[4][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	if pickaxechecker == 12:
		print("1. Stone")
		print("2. Coal")
		print("3. Chain")
		print("4. Brick")
		print("5. Iron")
		print("6. Steel")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[0][1],"stone")
			howmany = input("How much stone? ")
			if int(howmany) > int(inventory[0][1]):
				print("Not enough stone!!!")
			else:
				inventory[0][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[1][1],"coal")
			howmany = input("How much coal? ")
			if int(howmany) > int(inventory[1][1]):
				print("Not enough coal!!!")
			else:
				inventory[1][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[2][1],"chain")
			howmany = input("How much chain? ")
			if int(howmany) > int(inventory[2][1]):
				print("Not enough chain!")
			else:
				inventory[2][1] -= int(howmany)
				moneygained = int(howmany) * 5
				money += moneygained
				print("You got $"+ str(moneygained))
		elif sellchoice == "4":
			os.system("clear")
			print("You have",inventory[3][1],"brick")
			howmany = input("How much brick? ")
			if int(howmany) > int(inventory[3][1]):
				print("Not enough brick!")
			else:
				inventory[3][1] -= int(howmany)
				moneygained = int(howmany) * 7
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "5":
			os.system("clear")
			print("You have",inventory[4][1],"iron")
			howmany = input("How much iron? ")
			if int(howmany) > int(inventory[4][1]):
				print("Not enough iron!")
			else:
				inventory[4][1] -= int(howmany)
				moneygained = int(howmany) * 10
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "6":
			os.system("clear")
			print("You have",inventory[5][1],"steel")
			howmany = input("How much steel? ")
			if int(howmany) > int(inventory[5][1]):
				print("Not enough steel!")
			else:
				inventory[5][1] -= int(howmany)
				moneygained = int(howmany) * 15
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[0][1] * 1) + (inventory[1][1] * 2) + (inventory[2][1] * 5) + (inventory[3][1] * 7) + (inventory[4][1] * 10) + (inventory[5][1] * 15)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[0][1] -= inventory[0][1]
			inventory[1][1] -= inventory[1][1]
			inventory[2][1] -= inventory[2][1]
			inventory[3][1] -= inventory[3][1]
			inventory[4][1] -= inventory[4][1]
			inventory[5][1] -= inventory[5][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	if pickaxechecker == 14:
		print("1. Stone")
		print("2. Coal")
		print("3. Chain")
		print("4. Brick")
		print("5. Iron")
		print("6. Steel")
		print("7. Gold")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[0][1],"stone")
			howmany = input("How much stone? ")
			if int(howmany) > int(inventory[0][1]):
				print("Not enough stone!!!")
			else:
				inventory[0][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[1][1],"coal")
			howmany = input("How much coal? ")
			if int(howmany) > int(inventory[1][1]):
				print("Not enough coal!!!")
			else:
				inventory[1][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[2][1],"chain")
			howmany = input("How much chain? ")
			if int(howmany) > int(inventory[2][1]):
				print("Not enough chain!")
			else:
				inventory[2][1] -= int(howmany)
				moneygained = int(howmany) * 5
				money += moneygained
				print("You got $"+ str(moneygained))
		elif sellchoice == "4":
			os.system("clear")
			print("You have",inventory[3][1],"brick")
			howmany = input("How much brick? ")
			if int(howmany) > int(inventory[3][1]):
				print("Not enough brick!")
			else:
				inventory[3][1] -= int(howmany)
				moneygained = int(howmany) * 7
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "5":
			os.system("clear")
			print("You have",inventory[4][1],"iron")
			howmany = input("How much iron? ")
			if int(howmany) > int(inventory[4][1]):
				print("Not enough iron!")
			else:
				inventory[4][1] -= int(howmany)
				moneygained = int(howmany) * 10
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "6":
			os.system("clear")
			print("You have",inventory[5][1],"steel")
			howmany = input("How much steel? ")
			if int(howmany) > int(inventory[5][1]):
				print("Not enough steel!")
			else:
				inventory[5][1] -= int(howmany)
				moneygained = int(howmany) * 15
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "7":
			os.system("clear")
			print("You have",inventory[6][1],"gold")
			howmany = input("How much gold? ")
			if int(howmany) > int(inventory[6][1]):
				print("Not enough gold!")
			else:
				inventory[6][1] -= int(howmany)
				moneygained = int(howmany) * 20
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[0][1] * 1) + (inventory[1][1] * 2) + (inventory[2][1] * 5) + (inventory[3][1] * 7) + (inventory[4][1] * 10) + (inventory[5][1] * 15) + (inventory[6][1] * 20)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[0][1] -= inventory[0][1]
			inventory[1][1] -= inventory[1][1]
			inventory[2][1] -= inventory[2][1]
			inventory[3][1] -= inventory[3][1]
			inventory[4][1] -= inventory[4][1]
			inventory[5][1] -= inventory[5][1]
			inventory[6][1] -= inventory[6][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	if pickaxechecker == 16:
		print("1. Stone")
		print("2. Coal")
		print("3. Chain")
		print("4. Brick")
		print("5. Iron")
		print("6. Steel")
		print("7. Gold")
		print("8. Diamond")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[0][1],"stone")
			howmany = input("How much stone? ")
			if int(howmany) > int(inventory[0][1]):
				print("Not enough stone!!!")
			else:
				inventory[0][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[1][1],"coal")
			howmany = input("How much coal? ")
			if int(howmany) > int(inventory[1][1]):
				print("Not enough coal!!!")
			else:
				inventory[1][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[2][1],"chain")
			howmany = input("How much chain? ")
			if int(howmany) > int(inventory[2][1]):
				print("Not enough chain!")
			else:
				inventory[2][1] -= int(howmany)
				moneygained = int(howmany) * 5
				money += moneygained
				print("You got $"+ str(moneygained))
		elif sellchoice == "4":
			os.system("clear")
			print("You have",inventory[3][1],"brick")
			howmany = input("How much brick? ")
			if int(howmany) > int(inventory[3][1]):
				print("Not enough brick!")
			else:
				inventory[3][1] -= int(howmany)
				moneygained = int(howmany) * 7
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "5":
			os.system("clear")
			print("You have",inventory[4][1],"iron")
			howmany = input("How much iron? ")
			if int(howmany) > int(inventory[4][1]):
				print("Not enough iron!")
			else:
				inventory[4][1] -= int(howmany)
				moneygained = int(howmany) * 10
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "6":
			os.system("clear")
			print("You have",inventory[5][1],"steel")
			howmany = input("How much steel? ")
			if int(howmany) > int(inventory[5][1]):
				print("Not enough steel!")
			else:
				inventory[5][1] -= int(howmany)
				moneygained = int(howmany) * 15
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "7":
			os.system("clear")
			print("You have",inventory[6][1],"gold")
			howmany = input("How much gold? ")
			if int(howmany) > int(inventory[6][1]):
				print("Not enough gold!")
			else:
				inventory[6][1] -= int(howmany)
				moneygained = int(howmany) * 20
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "8":
			os.system("clear")
			print("You have",inventory[7][1],"diamonds")
			howmany = input("How much diamonds? ")
			if int(howmany) > int(inventory[7][1]):
				print("Not enough diamonds!")
			else:
				inventory[7][1] -= int(howmany)
				moneygained = int(howmany) * 25
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[0][1] * 1) + (inventory[1][1] * 2) + (inventory[2][1] * 5) + (inventory[3][1] * 7) + (inventory[4][1] * 10) + (inventory[5][1] * 15) + (inventory[6][1] * 20) + (inventory[7][1] * 25)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[0][1] -= inventory[0][1]
			inventory[1][1] -= inventory[1][1]
			inventory[2][1] -= inventory[2][1]
			inventory[3][1] -= inventory[3][1]
			inventory[4][1] -= inventory[4][1]
			inventory[5][1] -= inventory[5][1]
			inventory[6][1] -= inventory[6][1]
			inventory[7][1] -= inventory[7][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	if pickaxechecker == 18 or pickaxechecker == 20 or pickaxechecker == 22:
		print("1. Stone")
		print("2. Coal")
		print("3. Chain")
		print("4. Brick")
		print("5. Iron")
		print("6. Steel")
		print("7. Gold")
		print("8. Diamond")
		print("9. Emerald")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[0][1],"stone")
			howmany = input("How much stone? ")
			if int(howmany) > int(inventory[0][1]):
				print("Not enough stone!!!")
			else:
				inventory[0][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[1][1],"coal")
			howmany = input("How much coal? ")
			if int(howmany) > int(inventory[1][1]):
				print("Not enough coal!!!")
			else:
				inventory[1][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[2][1],"chain")
			howmany = input("How much chain? ")
			if int(howmany) > int(inventory[2][1]):
				print("Not enough chain!")
			else:
				inventory[2][1] -= int(howmany)
				moneygained = int(howmany) * 5
				money += moneygained
				print("You got $"+ str(moneygained))
		elif sellchoice == "4":
			os.system("clear")
			print("You have",inventory[3][1],"brick")
			howmany = input("How much brick? ")
			if int(howmany) > int(inventory[3][1]):
				print("Not enough brick!")
			else:
				inventory[3][1] -= int(howmany)
				moneygained = int(howmany) * 7
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "5":
			os.system("clear")
			print("You have",inventory[4][1],"iron")
			howmany = input("How much iron? ")
			if int(howmany) > int(inventory[4][1]):
				print("Not enough iron!")
			else:
				inventory[4][1] -= int(howmany)
				moneygained = int(howmany) * 10
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "6":
			os.system("clear")
			print("You have",inventory[5][1],"steel")
			howmany = input("How much steel? ")
			if int(howmany) > int(inventory[5][1]):
				print("Not enough steel!")
			else:
				inventory[5][1] -= int(howmany)
				moneygained = int(howmany) * 15
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "7":
			os.system("clear")
			print("You have",inventory[6][1],"gold")
			howmany = input("How much gold? ")
			if int(howmany) > int(inventory[6][1]):
				print("Not enough gold!")
			else:
				inventory[6][1] -= int(howmany)
				moneygained = int(howmany) * 20
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "8":
			os.system("clear")
			print("You have",inventory[7][1],"diamonds")
			howmany = input("How many diamonds? ")
			if int(howmany) > int(inventory[7][1]):
				print("Not enough gold!")
			else:
				inventory[7][1] -= int(howmany)
				moneygained = int(howmany) * 25
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "9":
			os.system("clear")
			print("You have",inventory[8][1],"emeralds")
			howmany = input("How many emeralds? ")
			if int(howmany) > int(inventory[8][1]):
				print("Not enough emeralds!")
			else:
				inventory[8][1] -= int(howmany)
				moneygained = int(howmany) * 50
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[0][1] * 1) + (inventory[1][1] * 2) + (inventory[2][1] * 5) + (inventory[3][1] * 7) + (inventory[4][1] * 10) + (inventory[5][1] * 15) + (inventory[6][1] * 20) + (inventory[7][1] * 25) + (inventory[8][1] * 50)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[0][1] -= inventory[0][1]
			inventory[1][1] -= inventory[1][1]
			inventory[2][1] -= inventory[2][1]
			inventory[3][1] -= inventory[3][1]
			inventory[4][1] -= inventory[4][1]
			inventory[5][1] -= inventory[5][1]
			inventory[6][1] -= inventory[6][1]
			inventory[7][1] -= inventory[7][1]
			inventory[8][1] -= inventory[8][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	if quests[2][3] < 10:
		if sellchoice == "1":
			if inventory[0][1] > howmany:
				quests[2][3] += howmany
	if pickaxechecker == 24:
		print("1. Netherrack")
		print("2. Gold Nuggets")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[9][1],"netherrack")
			howmany = input("How much netherrack? ")
			if int(howmany) > int(inventory[9][1]):
				print("Not enough netherrack!!!")
			else:
				inventory[9][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[10][1],"gold nuggets")
			howmany = input("How much gold nuggets? ")
			if int(howmany) > int(inventory[10][1]):
				print("Not enough gold nuggets!!!")
			else:
				inventory[10][1] -= int(howmany)
				moneygained = int(howmany) * 2
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[9][1] * 1) + (inventory[10][1] * 2)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[9][1] -= inventory[9][1]
			inventory[10][1] -= inventory[10][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	elif pickaxechecker == 26:
		print("1. Netherrack")
		print("2. Gold Nuggets")
		print("3. Quartz")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[9][1],"netherrack")
			howmany = input("How much netherrack? ")
			if int(howmany) > int(inventory[9][1]):
				print("Not enough netherrack!!!")
			else:
				inventory[9][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[10][1],"gold nuggets")
			howmany = input("How much gold nuggets? ")
			if int(howmany) > int(inventory[10][1]):
				print("Not enough gold nuggets!!!")
			else:
				inventory[10][1] -= int(howmany)
				moneygained = int(howmany) * 2
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[11][1],"quartz")
			howmany = input("How much quartz? ")
			if int(howmany) > int(inventory[11][1]):
				print("Not enough quartz!!!")
			else:
				inventory[11][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[9][1] * 1) + (inventory[10][1] * 2) + (inventory[11][1] * 3)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[9][1] -= inventory[9][1]
			inventory[10][1] -= inventory[10][1]
			inventory[11][1] -= inventory[11][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	elif pickaxechecker == 28:
		print("1. Netherrack")
		print("2. Gold Nuggets")
		print("3. Quartz")
		print("4. Gold")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[9][1],"netherrack")
			howmany = input("How much netherrack? ")
			if int(howmany) > int(inventory[9][1]):
				print("Not enough netherrack!!!")
			else:
				inventory[9][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[10][1],"gold nuggets")
			howmany = input("How much gold nuggets? ")
			if int(howmany) > int(inventory[10][1]):
				print("Not enough gold nuggets!!!")
			else:
				inventory[10][1] -= int(howmany)
				moneygained = int(howmany) * 2
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[11][1],"quartz")
			howmany = input("How much quartz? ")
			if int(howmany) > int(inventory[11][1]):
				print("Not enough quartz!!!")
			else:
				inventory[11][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "4":
			os.system("clear")
			print("You have",inventory[12][1],"gold")
			howmany = input("How much gold? ")
			if int(howmany) > int(inventory[12][1]):
				print("Not enough gold!!!")
			else:
				inventory[12][1] -= int(howmany)
				moneygained = int(howmany) * 5
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[9][1] * 1) + (inventory[10][1] * 2) + (inventory[11][1] * 3) + (inventory[12][1] * 5)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[9][1] -= inventory[9][1]
			inventory[10][1] -= inventory[10][1]
			inventory[11][1] -= inventory[11][1]
			inventory[12][1] -= inventory[12][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	elif pickaxechecker == 30:
		print("1. Netherrack")
		print("2. Gold Nuggets")
		print("3. Quartz")
		print("4. Gold")
		print("5. Ancient Debris")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[9][1],"netherrack")
			howmany = input("How much netherrack? ")
			if int(howmany) > int(inventory[9][1]):
				print("Not enough netherrack!!!")
			else:
				inventory[9][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[10][1],"gold nuggets")
			howmany = input("How much gold nuggets? ")
			if int(howmany) > int(inventory[10][1]):
				print("Not enough gold nuggets!!!")
			else:
				inventory[10][1] -= int(howmany)
				moneygained = int(howmany) * 2
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[11][1],"quartz")
			howmany = input("How much quartz? ")
			if int(howmany) > int(inventory[11][1]):
				print("Not enough quartz!!!")
			else:
				inventory[11][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "4":
			os.system("clear")
			print("You have",inventory[12][1],"gold")
			howmany = input("How much gold? ")
			if int(howmany) > int(inventory[12][1]):
				print("Not enough gold!!!")
			else:
				inventory[12][1] -= int(howmany)
				moneygained = int(howmany) * 5
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "5":
			os.system("clear")
			print("You have",inventory[13][1],"ancient debris")
			howmany = input("How much ancient debris? ")
			if int(howmany) > int(inventory[13][1]):
				print("Not enough ancient debris!!!")
			else:
				inventory[13][1] -= int(howmany)
				moneygained = int(howmany) * 7
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[9][1] * 1) + (inventory[10][1] * 2) + (inventory[11][1] * 3) + (inventory[12][1] * 5) + (inventory[13][1] * 7)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[9][1] -= inventory[9][1]
			inventory[10][1] -= inventory[10][1]
			inventory[11][1] -= inventory[11][1]
			inventory[12][1] -= inventory[12][1]
			inventory[13][1] -= inventory[13][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	elif pickaxechecker == 32:
		print("1. Netherrack")
		print("2. Gold Nuggets")
		print("3. Quartz")
		print("4. Gold")
		print("5. Ancient Debris")
		print("6. Netherite Scrap")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[9][1],"netherrack")
			howmany = input("How much netherrack? ")
			if int(howmany) > int(inventory[9][1]):
				print("Not enough netherrack!!!")
			else:
				inventory[9][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[10][1],"gold nuggets")
			howmany = input("How much gold nuggets? ")
			if int(howmany) > int(inventory[10][1]):
				print("Not enough gold nuggets!!!")
			else:
				inventory[10][1] -= int(howmany)
				moneygained = int(howmany) * 2
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[11][1],"quartz")
			howmany = input("How much quartz? ")
			if int(howmany) > int(inventory[11][1]):
				print("Not enough quartz!!!")
			else:
				inventory[11][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "4":
			os.system("clear")
			print("You have",inventory[12][1],"gold")
			howmany = input("How much gold? ")
			if int(howmany) > int(inventory[12][1]):
				print("Not enough gold!!!")
			else:
				inventory[12][1] -= int(howmany)
				moneygained = int(howmany) * 5
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "5":
			os.system("clear")
			print("You have",inventory[13][1],"ancient debris")
			howmany = input("How much ancient debris? ")
			if int(howmany) > int(inventory[13][1]):
				print("Not enough ancient debris!!!")
			else:
				inventory[13][1] -= int(howmany)
				moneygained = int(howmany) * 7
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "6":
			os.system("clear")
			print("You have",inventory[14][1],"netherite scraps")
			howmany = input("How many netherite scraps? ")
			if int(howmany) > int(inventory[14][1]):
				print("Not enough netherite scraps!!!")
			else:
				inventory[14][1] -= int(howmany)
				moneygained = int(howmany) * 10
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[9][1] * 1) + (inventory[10][1] * 2) + (inventory[11][1] * 3) + (inventory[12][1] * 5) + (inventory[13][1] * 7) + (inventory[14][1] * 10)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[9][1] -= inventory[9][1]
			inventory[10][1] -= inventory[10][1]
			inventory[11][1] -= inventory[11][1]
			inventory[12][1] -= inventory[12][1]
			inventory[13][1] -= inventory[13][1]
			inventory[14][1] -= inventory[14][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	elif pickaxechecker == 34 or pickaxechecker == 36 or pickaxechecker == 38:
		print("1. Netherrack")
		print("2. Gold Nuggets")
		print("3. Quartz")
		print("4. Gold")
		print("5. Ancient Debris")
		print("6. Netherite Scrap")
		print("7. Netherite Ingot")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[9][1],"netherrack")
			howmany = input("How much netherrack? ")
			if int(howmany) > int(inventory[9][1]):
				print("Not enough netherrack!!!")
			else:
				inventory[9][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[10][1],"gold nuggets")
			howmany = input("How much gold nuggets? ")
			if int(howmany) > int(inventory[10][1]):
				print("Not enough gold nuggets!!!")
			else:
				inventory[10][1] -= int(howmany)
				moneygained = int(howmany) * 2
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[11][1],"quartz")
			howmany = input("How much quartz? ")
			if int(howmany) > int(inventory[11][1]):
				print("Not enough quartz!!!")
			else:
				inventory[11][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "4":
			os.system("clear")
			print("You have",inventory[12][1],"gold")
			howmany = input("How much gold? ")
			if int(howmany) > int(inventory[12][1]):
				print("Not enough gold!!!")
			else:
				inventory[12][1] -= int(howmany)
				moneygained = int(howmany) * 5
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "5":
			os.system("clear")
			print("You have",inventory[13][1],"ancient debris")
			howmany = input("How much ancient debris? ")
			if int(howmany) > int(inventory[13][1]):
				print("Not enough ancient debris!!!")
			else:
				inventory[13][1] -= int(howmany)
				moneygained = int(howmany) * 7
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "6":
			os.system("clear")
			print("You have",inventory[14][1],"netherite scraps")
			howmany = input("How many netherite scraps? ")
			if int(howmany) > int(inventory[14][1]):
				print("Not enough netherite scraps!!!")
			else:
				inventory[14][1] -= int(howmany)
				moneygained = int(howmany) * 10
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "7":
			os.system("clear")
			print("You have",inventory[15][1],"netherite ingots")
			howmany = input("How many netherite ingots? ")
			if int(howmany) > int(inventory[15][1]):
				print("Not enough netherite ingots!!!")
			else:
				inventory[15][1] -= int(howmany)
				moneygained = int(howmany) * 12
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[9][1] * 1) + (inventory[10][1] * 2) + (inventory[11][1] * 3) + (inventory[12][1] * 5) + (inventory[13][1] * 7) + (inventory[14][1] * 10) + (inventory[15][1] * 12)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[9][1] -= inventory[9][1]
			inventory[10][1] -= inventory[10][1]
			inventory[11][1] -= inventory[11][1]
			inventory[12][1] -= inventory[12][1]
			inventory[13][1] -= inventory[13][1]
			inventory[14][1] -= inventory[14][1]
			inventory[15][1] -= inventory[15][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	elif pickaxechecker == 40:
		print("1. Endstone")
		print("2. Endbrick")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[16][1],"endstone")
			howmany = input("How much endstone? ")
			if int(howmany) > int(inventory[16][1]):
				print("Not enough endstone!!!")
			else:
				inventory[16][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[17][1],"endbricks")
			howmany = input("How much endbricks? ")
			if int(howmany) > int(inventory[17][1]):
				print("Not enough endbricks!!!")
			else:
				inventory[17][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[16][1] * 1) + (inventory[17][1] * 3)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[16][1] -= inventory[16][1]
			inventory[17][1] -= inventory[17][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	elif pickaxechecker == 42:
		print("1. Endstone")
		print("2. Endbrick")
		print("3. Purpur")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[16][1],"endstone")
			howmany = input("How much endstone? ")
			if int(howmany) > int(inventory[16][1]):
				print("Not enough endstone!!!")
			else:
				inventory[16][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[17][1],"endbricks")
			howmany = input("How much endbricks? ")
			if int(howmany) > int(inventory[17][1]):
				print("Not enough endbricks!!!")
			else:
				inventory[17][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[18][1],"purpur")
			howmany = input("How much purpur? ")
			if int(howmany) > int(inventory[18][1]):
				print("Not enough purpur!!!")
			else:
				inventory[18][1] -= int(howmany)
				moneygained = int(howmany) * 5
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[16][1] * 1) + (inventory[17][1] * 3) + (inventory[18][1] * 5)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[16][1] -= inventory[16][1]
			inventory[17][1] -= inventory[17][1]
			inventory[18][1] -= inventory[18][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	elif pickaxechecker == 44:
		print("1. Endstone")
		print("2. Endbrick")
		print("3. Purpur")
		print("4. Unbreakable Endstone")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[16][1],"endstone")
			howmany = input("How much endstone? ")
			if int(howmany) > int(inventory[16][1]):
				print("Not enough endstone!!!")
			else:
				inventory[16][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[17][1],"endbricks")
			howmany = input("How much endbricks? ")
			if int(howmany) > int(inventory[17][1]):
				print("Not enough endbricks!!!")
			else:
				inventory[17][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[18][1],"purpur")
			howmany = input("How much purpur? ")
			if int(howmany) > int(inventory[18][1]):
				print("Not enough purpur!!!")
			else:
				inventory[18][1] -= int(howmany)
				moneygained = int(howmany) * 5
		elif sellchoice == "4":
			os.system("clear")
			print("You have",inventory[19][1],"unbreakable endstone")
			howmany = input("How much unbreakable endstone? ")
			if int(howmany) > int(inventory[19][1]):
				print("Not enough unbreakable endstone!!!")
			else:
				inventory[19][1] -= int(howmany)
				moneygained = int(howmany) * 10
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[16][1] * 1) + (inventory[17][1] * 3) + (inventory[18][1] * 5) + (inventory[19][1] * 10)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[16][1] -= inventory[16][1]
			inventory[17][1] -= inventory[17][1]
			inventory[18][1] -= inventory[18][1]
			inventory[19][1] -= inventory[19][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	elif pickaxechecker == 46 or pickaxechecker == 48:
		print("1. Endstone")
		print("2. Endbrick")
		print("3. Purpur")
		print("4. Unbreakable Endstone")
		print("5. Ender Dragon Pieces")
		sellchoice = input("What to sell? ")
		if sellchoice == "1":
			os.system("clear")
			print("You have",inventory[16][1],"endstone")
			howmany = input("How much endstone? ")
			if int(howmany) > int(inventory[16][1]):
				print("Not enough endstone!!!")
			else:
				inventory[16][1] -= int(howmany)
				moneygained = int(howmany)
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "2":
			os.system("clear")
			print("You have",inventory[17][1],"endbricks")
			howmany = input("How much endbricks? ")
			if int(howmany) > int(inventory[17][1]):
				print("Not enough endbricks!!!")
			else:
				inventory[17][1] -= int(howmany)
				moneygained = int(howmany) * 3
				money += moneygained
				print("You got $" + str(moneygained))
		elif sellchoice == "3":
			os.system("clear")
			print("You have",inventory[18][1],"purpur")
			howmany = input("How much purpur? ")
			if int(howmany) > int(inventory[18][1]):
				print("Not enough purpur!!!")
			else:
				inventory[18][1] -= int(howmany)
				moneygained = int(howmany) * 5
		elif sellchoice == "4":
			os.system("clear")
			print("You have",inventory[19][1],"unbreakable endstone")
			howmany = input("How much unbreakable endstone? ")
			if int(howmany) > int(inventory[19][1]):
				print("Not enough unbreakable endstone!!!")
			else:
				inventory[19][1] -= int(howmany)
				moneygained = int(howmany) * 10
		elif sellchoice == "5":
			os.system("clear")
			print("You have",inventory[20][1],"ender dragon pieces")
			howmany = input("How much ender dragon pieces? ")
			if int(howmany) > int(inventory[20][1]):
				print("Not enough ender dragon pieces!!!")
			else:
				inventory[20][1] -= int(howmany)
				moneygained = int(howmany) * 25
		elif sellchoice == "0":
			os.system("clear")
			moneygained = (inventory[16][1] * 1) + (inventory[17][1] * 3) + (inventory[18][1] * 5) + (inventory[19][1] * 10) + (inventory[20][1] * 25)
			money += moneygained
			print("You got $"+str(moneygained))
			inventory[16][1] -= inventory[16][1]
			inventory[17][1] -= inventory[17][1]
			inventory[18][1] -= inventory[18][1]
			inventory[19][1] -= inventory[19][1]
			inventory[20][1] -= inventory[20][1]
		else:
			os.system("clear")
			print("Not a valid option!")
		input("Press [enter] to continue")
	return pickaxes,pickaxe,inventory,money,enchantments,quests