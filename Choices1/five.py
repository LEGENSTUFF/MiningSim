import os
def five(pickaxe,pickaxes,money):
	os.system("clear")
	if pickaxe == "Wooden Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[0][1] + int(howmuch)) > 59:
				print("Durability over limit!")
			elif (pickaxes[0][1] + int(howmuch)) <= 59:
				if money >= int(howmuch):
					pickaxes[0][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Stone Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[1][1] + int(howmuch)) > 131:
				print("Durability over limit!")
			elif (pickaxes[1][1] + int(howmuch)) <= 131:
				if money >= int(howmuch):
					pickaxes[1][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Coal Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[2][1] + int(howmuch)) > 200:
				print("Durability over limit!")
			elif (pickaxes[2][1] + int(howmuch)) <= 200:
				if money >= int(howmuch):
					pickaxes[2][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Chain Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[3][1] + int(howmuch)) > 250:
				print("Durability over limit!")
			elif (pickaxes[3][1] + int(howmuch)) <= 250:
				if money >= int(howmuch):
					pickaxes[3][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Brick Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[4][1] + int(howmuch)) > 300:
				print("Durability over limit!")
			elif (pickaxes[4][1] + int(howmuch)) <= 300:
				if money >= int(howmuch):
					pickaxes[4][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Iron Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[5][1] + int(howmuch)) > 350:
				print("Durability over limit!")
			elif (pickaxes[5][1] + int(howmuch)) <= 350:
				if money >= int(howmuch):
					pickaxes[5][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Steel Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[6][1] + int(howmuch)) > 400:
				print("Durability over limit!")
			elif (pickaxes[6][1] + int(howmuch)) <= 400:
				if money >= int(howmuch):
					pickaxes[6][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Gold Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[7][1] + int(howmuch)) > 500:
				print("Durability over limit!")
			elif (pickaxes[7][1] + int(howmuch)) <= 500:
				if money >= int(howmuch):
					pickaxes[7][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Diamond Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[8][1] + int(howmuch)) > 750:
				print("Durability over limit!")
			elif (pickaxes[8][1] + int(howmuch)) <= 750:
				if money >= int(howmuch):
					pickaxes[8][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Emerald Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[9][1] + int(howmuch)) > 1000:
				print("Durability over limit!")
			elif (pickaxes[9][1] + int(howmuch)) <= 1000:
				if money >= int(howmuch):
					pickaxes[9][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Netherrack Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[11][1] + int(howmuch)) > 100:
				print("Durability over limit!")
			elif (pickaxes[11][1] + int(howmuch)) <= 100:
				if money >= int(howmuch):
					pickaxes[11][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Gold nugget Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[12][1] + int(howmuch)) > 250:
				print("Durability over limit!")
			elif (pickaxes[12][1] + int(howmuch)) <= 250:
				if money >= int(howmuch):
					pickaxes[12][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Quartz Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[13][1] + int(howmuch)) > 500:
				print("Durability over limit!")
			elif (pickaxes[13][1] + int(howmuch)) <= 500:
				if money >= int(howmuch):
					pickaxes[13][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Quartz and Gold Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[14][1] + int(howmuch)) > 750:
				print("Durability over limit!")
			elif (pickaxes[14][1] + int(howmuch)) <= 750:
				if money >= int(howmuch):
					pickaxes[14][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Ancient Debris Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[15][1] + int(howmuch)) > 1000:
				print("Durability over limit!")
			elif (pickaxes[15][1] + int(howmuch)) <= 1000:
				if money >= int(howmuch):
					pickaxes[15][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Netherite Ingot Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[16][1] + int(howmuch)) > 1500:
				print("Durability over limit!")
			elif (pickaxes[16][1] + int(howmuch)) <= 1500:
				if money >= int(howmuch):
					pickaxes[16][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Netherite Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[17][1] + int(howmuch)) > 1500:
				print("Durability over limit!")
			elif (pickaxes[17][1] + int(howmuch)) <= 1500:
				if money >= int(howmuch):
					pickaxes[17][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Endstone Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[19][1] + int(howmuch)) > 500:
				print("Durability over limit!")
			elif (pickaxes[19][1] + int(howmuch)) <= 500:
				if money >= int(howmuch):
					pickaxes[19][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "End Brick Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[20][1] + int(howmuch)) > 1000:
				print("Durability over limit!")
			elif (pickaxes[20][1] + int(howmuch)) <= 1000:
				if money >= int(howmuch):
					pickaxes[20][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Purpur Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[21][1] + int(howmuch)) > 2500:
				print("Durability over limit!")
			elif (pickaxes[21][1] + int(howmuch)) <= 2500:
				if money >= int(howmuch):
					pickaxes[21][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Unbreakable Endstone Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[22][1] + int(howmuch)) > 5000:
				print("Durability over limit!")
			elif (pickaxes[22][1] + int(howmuch)) <= 5000:
				if money >= int(howmuch):
					pickaxes[22][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	elif pickaxe == "Ender Dragon Pickaxe":
		print("Your pickaxe will be repaired now")
		print("1. Yes")
		print("2. No")
		repairchoice = input("Choose an option ")
		os.system("clear")
		if repairchoice == "1":
			howmuch = input("How much durability? ")
			if (pickaxes[23][1] + int(howmuch)) > 10000:
				print("Durability over limit!")
			elif (pickaxes[23][1] + int(howmuch)) <= 10000:
				if money >= int(howmuch):
					pickaxes[23][1] += int(howmuch)
					money -= int(howmuch)
					print("Your pickaxe got repaired by", howmuch, "durability")
				else:
					print("Not enough money!")
	sidequests[2][2] -= int(howmuch)
	input("Press [enter] to continue")
	return pickaxe,pickaxes,money