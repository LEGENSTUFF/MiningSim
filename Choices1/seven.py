import os
def seven(stars,level,skins):
	os.system("clear")
	print("Next season in 12 days! (Last updated: 6th July 2023)")
	print("Level:",level)
	print("Stars:",stars)
	print("Max level: 30")
	if level == 1 or level == 2 or level == 3 or level == 4 or level == 5 or level == 6 or level == 7 or level == 8:
		print("Stars required to level up: 1")
		if stars >= 1:
			print("Would you like to level up? (Y/N)")
			choice = input("")
			if choice == "Y":
				level += 1
				stars -= 1
	elif level == 9:
		print("Stars required to level up: 2")
		if stars >= 2:
			print("Would you like to level up? (Y/N)")
			choice = input("")
			if choice == "Y":
				print("SKIN UNLOCKED: MINER")
				skins.append(["Miner","Uncommon"])
				level += 1
				stars -= 2
	elif level == 10 or level == 11 or level == 12 or level == 13 or level == 14 or level == 15 or level == 16 or level == 17 or level == 18:
		print("Stars required to level up: 2")
		if stars >= 2:
			print("Would you like to level up? (Y/N)")
			choice = input("")
			if choice == "Y":
				level += 1
				stars -= 2
	elif level == 19:
		print("Stars required to level up: 3")
		if stars >= 3:
			print("Would you like to level up? (Y/N)")
			choice = input("")
			if choice == "Y":
				print("SKIN UNLOCKED: COLLECTOR")
				skins.append(["Collector","Epic"])
				level += 1
				stars -= 3
	elif level == 20 or level == 21 or level == 22 or level == 23 or level == 24:
		print("Stars required to level up: 3")
		if stars >= 3:
			print("Would you like to level up? (Y/N)")
			choice = input("")
			if choice == "Y":
				level += 1
				stars -= 3
	elif level == 25 or level == 26 or level == 27 or level == 28:
		print("Stars required to level up: 4")
		if stars >= 4:
			print("Would you like to level up? (Y/N)")
			choice = input("")
			if choice == "Y":
				level += 1
				stars -= 4
	elif level == 29:
		print("Stars required to level up: 5")
		if stars >= 5:
			print("Would you like to level up? (Y/N)")
			choice = input("")
			if choice == "Y":
				print("SKIN UNLOCKED: CURATOR")
				skins.append(["Curator","Legendary"])
				level += 1
				stars -= 5
	elif level == 30:
		print("MAX LEVEL! GG!")
	print("Press [enter] to continue")
	return stars,level,skins