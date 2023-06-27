import os
def four(pickaxe,pickaxes):
	os.system("clear")
	pickaxechecker = sum(len(l) for l in pickaxes)
	if pickaxechecker == 2:
		print("1. Wooden Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Wooden Pickaxe":
				print("This pickaxe is already equipped!")
	elif pickaxechecker == 4:
		print("1. Wooden Pickaxe")
		print("2. Stone Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Wooden Pickaxe":
				print("This pickaxe is already equipped")
			elif pickaxe == "Stone Pickaxe":
				pickaxe = "Wooden Pickaxe"
				print("Wooden Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Wooden Pickaxe":
				pickaxe = "Stone Pickaxe"
				print("Stone Pickaxe equipped!")
			elif pickaxe == "Stone Pickaxe":
				print("This pickaxe is already equipped")
	elif pickaxechecker == 6:
		print("1. Wooden Pickaxe")
		print("2. Stone Pickaxe")
		print("3. Coal Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Wooden Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Wooden Pickaxe"
				print("Wooden Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Stone Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Stone Pickaxe"
				print("Stone Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Coal Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Coal Pickaxe"
				print("Coal Pickaxe equipped!")
	elif pickaxechecker == 6:
		print("1. Wooden Pickaxe")
		print("2. Stone Pickaxe")
		print("3. Coal Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Wooden Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Wooden Pickaxe"
				print("Wooden Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Stone Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Stone Pickaxe"
				print("Stone Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Coal Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Coal Pickaxe"
				print("Coal Pickaxe equipped!")
	elif pickaxechecker == 8:
		print("1. Wooden Pickaxe")
		print("2. Stone Pickaxe")
		print("3. Coal Pickaxe")
		print("4. Chain Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Wooden Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Wooden Pickaxe"
				print("Wooden Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Stone Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Stone Pickaxe"
				print("Stone Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Coal Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Coal Pickaxe"
				print("Coal Pickaxe equipped!")
		elif equipchoice == "4":
			if pickaxe == "Chain Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Chain Pickaxe"
				print("Chain Pickaxe equipped!")
	elif pickaxechecker == 10:
		print("1. Wooden Pickaxe")
		print("2. Stone Pickaxe")
		print("3. Coal Pickaxe")
		print("4. Chain Pickaxe")
		print("5. Brick Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Wooden Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Wooden Pickaxe"
				print("Wooden Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Stone Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Stone Pickaxe"
				print("Stone Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Coal Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Coal Pickaxe"
				print("Coal Pickaxe equipped!")
		elif equipchoice == "4":
			if pickaxe == "Chain Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Chain Pickaxe"
				print("Chain Pickaxe equipped!")
		elif equipchoice == "5":
			if pickaxe == "Brick Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Brick Pickaxe"
				print("Brick Pickaxe equipped!")
	elif pickaxechecker == 12:
		print("1. Wooden Pickaxe")
		print("2. Stone Pickaxe")
		print("3. Coal Pickaxe")
		print("4. Chain Pickaxe")
		print("5. Brick Pickaxe")
		print("6. Iron Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Wooden Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Wooden Pickaxe"
				print("Wooden Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Stone Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Stone Pickaxe"
				print("Stone Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Coal Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Coal Pickaxe"
				print("Coal Pickaxe equipped!")
		elif equipchoice == "4":
			if pickaxe == "Chain Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Chain Pickaxe"
				print("Chain Pickaxe equipped!")
		elif equipchoice == "5":
			if pickaxe == "Brick Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Brick Pickaxe"
				print("Brick Pickaxe equipped!")
		elif equipchoice == "6":
			if pickaxe == "Iron Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Iron Pickaxe"
				print("Iron Pickaxe equipped!")
	elif pickaxechecker == 14:
		print("1. Wooden Pickaxe")
		print("2. Stone Pickaxe")
		print("3. Coal Pickaxe")
		print("4. Chain Pickaxe")
		print("5. Brick Pickaxe")
		print("6. Iron Pickaxe")
		print("7. Steel Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Wooden Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Wooden Pickaxe"
				print("Wooden Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Stone Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Stone Pickaxe"
				print("Stone Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Coal Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Coal Pickaxe"
				print("Coal Pickaxe equipped!")
		elif equipchoice == "4":
			if pickaxe == "Chain Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Chain Pickaxe"
				print("Chain Pickaxe equipped!")
		elif equipchoice == "5":
			if pickaxe == "Brick Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Brick Pickaxe"
				print("Brick Pickaxe equipped!")
		elif equipchoice == "6":
			if pickaxe == "Iron Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Iron Pickaxe"
				print("Iron Pickaxe equipped!")
		elif equipchoice == "7":
			if pickaxe == "Steel Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Steel Pickaxe"
				print("Steel Pickaxe equipped!")
	elif pickaxechecker == 16:
		print("1. Wooden Pickaxe")
		print("2. Stone Pickaxe")
		print("3. Coal Pickaxe")
		print("4. Chain Pickaxe")
		print("5. Brick Pickaxe")
		print("6. Iron Pickaxe")
		print("7. Steel Pickaxe")
		print("8. Gold Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Wooden Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Wooden Pickaxe"
				print("Wooden Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Stone Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Stone Pickaxe"
				print("Stone Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Coal Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Coal Pickaxe"
				print("Coal Pickaxe equipped!")
		elif equipchoice == "4":
			if pickaxe == "Chain Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Chain Pickaxe"
				print("Chain Pickaxe equipped!")
		elif equipchoice == "5":
			if pickaxe == "Brick Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Brick Pickaxe"
				print("Brick Pickaxe equipped!")
		elif equipchoice == "6":
			if pickaxe == "Iron Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Iron Pickaxe"
				print("Iron Pickaxe equipped!")
		elif equipchoice == "7":
			if pickaxe == "Steel Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Steel Pickaxe"
				print("Steel Pickaxe equipped!")
		elif equipchoice == "8":
			if pickaxe == "Gold Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Gold Pickaxe"
				print("Gold Pickaxe equipped!")
	elif pickaxechecker == 18:
		print("1. Wooden Pickaxe")
		print("2. Stone Pickaxe")
		print("3. Coal Pickaxe")
		print("4. Chain Pickaxe")
		print("5. Brick Pickaxe")
		print("6. Iron Pickaxe")
		print("7. Steel Pickaxe")
		print("8. Gold Pickaxe")
		print("9. Diamond Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Wooden Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Wooden Pickaxe"
				print("Wooden Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Stone Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Stone Pickaxe"
				print("Stone Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Coal Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Coal Pickaxe"
				print("Coal Pickaxe equipped!")
		elif equipchoice == "4":
			if pickaxe == "Chain Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Chain Pickaxe"
				print("Chain Pickaxe equipped!")
		elif equipchoice == "5":
			if pickaxe == "Brick Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Brick Pickaxe"
				print("Brick Pickaxe equipped!")
		elif equipchoice == "6":
			if pickaxe == "Iron Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Iron Pickaxe"
				print("Iron Pickaxe equipped!")
		elif equipchoice == "7":
			if pickaxe == "Steel Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Steel Pickaxe"
				print("Steel Pickaxe equipped!")
		elif equipchoice == "8":
			if pickaxe == "Gold Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Gold Pickaxe"
				print("Gold Pickaxe equipped!")
		elif equipchoice == "9":
			if pickaxe == "Diamond Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Diamond Pickaxe"
				print("Diamond Pickaxe equipped!")
	elif pickaxechecker == 20 or pickaxechecker == 22:
		print("1. Wooden Pickaxe")
		print("2. Stone Pickaxe")
		print("3. Coal Pickaxe")
		print("4. Chain Pickaxe")
		print("5. Brick Pickaxe")
		print("6. Iron Pickaxe")
		print("7. Steel Pickaxe")
		print("8. Gold Pickaxe")
		print("9. Diamond Pickaxe")
		print("10. Emerald Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Wooden Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Wooden Pickaxe"
				print("Wooden Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Stone Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Stone Pickaxe"
				print("Stone Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Coal Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Coal Pickaxe"
				print("Coal Pickaxe equipped!")
		elif equipchoice == "4":
			if pickaxe == "Chain Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Chain Pickaxe"
				print("Chain Pickaxe equipped!")
		elif equipchoice == "5":
			if pickaxe == "Brick Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Brick Pickaxe"
				print("Brick Pickaxe equipped!")
		elif equipchoice == "6":
			if pickaxe == "Iron Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Iron Pickaxe"
				print("Iron Pickaxe equipped!")
		elif equipchoice == "7":
			if pickaxe == "Steel Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Steel Pickaxe"
				print("Steel Pickaxe equipped!")
		elif equipchoice == "8":
			if pickaxe == "Gold Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Gold Pickaxe"
				print("Gold Pickaxe equipped!")
		elif equipchoice == "9":
			if pickaxe == "Diamond Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Diamond Pickaxe"
				print("Diamond Pickaxe equipped!")
		elif equipchoice == "10":
			if pickaxe == "Emerald Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Emerald Pickaxe"
				print("Emerald Pickaxe equipped!")
	elif pickaxechecker == 24:
		print("1. Netherrack Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Netherrack Pickaxe":
				print("This pickaxe is already equipped!")
	elif pickaxechecker == 26:
		print("1. Netherrack Pickaxe")
		print("2. Gold nugget Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Netherrack Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Netherrack Pickaxe"
				print("Netherrack Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Gold nugget Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Gold nugget Pickaxe"
				print("Gold nugget Pickaxe equipped!")
	elif pickaxechecker == 28:
		print("1. Netherrack Pickaxe")
		print("2. Gold nugget Pickaxe")
		print("3. Quartz Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Netherrack Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Netherrack Pickaxe"
				print("Netherrack Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Gold nugget Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Gold nugget Pickaxe"
				print("Gold nugget Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Quartz Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Quartz Pickaxe"
				print("Quartz Pickaxe equipped!")
	elif pickaxechecker == 30:
		print("1. Netherrack Pickaxe")
		print("2. Gold nugget Pickaxe")
		print("3. Quartz Pickaxe")
		print("4. Quartz and Gold Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Netherrack Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Netherrack Pickaxe"
				print("Netherrack Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Gold nugget Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Gold nugget Pickaxe"
				print("Gold nugget Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Quartz Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Quartz Pickaxe"
				print("Quartz Pickaxe equipped!")
		elif equipchoice == "4":
			if pickaxe == "Quartz and Gold Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Quartz and Gold Pickaxe"
				print("Quartz and Gold Pickaxe equipped!")
	elif pickaxechecker == 32:
		print("1. Netherrack Pickaxe")
		print("2. Gold nugget Pickaxe")
		print("3. Quartz Pickaxe")
		print("4. Quartz and Gold Pickaxe")
		print("5. Ancient Debris Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Netherrack Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Netherrack Pickaxe"
				print("Netherrack Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Gold nugget Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Gold nugget Pickaxe"
				print("Gold nugget Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Quartz Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Quartz Pickaxe"
				print("Quartz Pickaxe equipped!")
		elif equipchoice == "4":
			if pickaxe == "Quartz and Gold Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Quartz and Gold Pickaxe"
				print("Quartz and Gold Pickaxe equipped!")
		elif equipchoice == "5":
			if pickaxe == "Ancient Debris Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Ancient Debris Pickaxe"
				print("Ancient Debris Pickaxe equipped!")
	elif pickaxechecker == 34:
		print("1. Netherrack Pickaxe")
		print("2. Gold nugget Pickaxe")
		print("3. Quartz Pickaxe")
		print("4. Quartz and Gold Pickaxe")
		print("5. Ancient Debris Pickaxe")
		print("6. Netherite Scrap Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Netherrack Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Netherrack Pickaxe"
				print("Netherrack Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Gold nugget Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Gold nugget Pickaxe"
				print("Gold nugget Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Quartz Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Quartz Pickaxe"
				print("Quartz Pickaxe equipped!")
		elif equipchoice == "4":
			if pickaxe == "Quartz and Gold Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Quartz and Gold Pickaxe"
				print("Quartz and Gold Pickaxe equipped!")
		elif equipchoice == "5":
			if pickaxe == "Ancient Debris Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Ancient Debris Pickaxe"
				print("Ancient Debris Pickaxe equipped!")
		elif equipchoice == "6":
			if pickaxe == "Netherite Scrap Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Netherite Scrap Pickaxe"
				print("Netherite Scrap Pickaxe equipped!")
	elif pickaxechecker == 36 or pickaxechecker == 38:
		print("1. Netherrack Pickaxe")
		print("2. Gold nugget Pickaxe")
		print("3. Quartz Pickaxe")
		print("4. Quartz and Gold Pickaxe")
		print("5. Ancient Debris Pickaxe")
		print("6. Netherite Scrap Pickaxe")
		print("7. Netherite Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Netherrack Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Netherrack Pickaxe"
				print("Netherrack Pickaxe equipped!")
		elif equipchoice == "2":
			if pickaxe == "Gold nugget Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Gold nugget Pickaxe"
				print("Gold nugget Pickaxe equipped!")
		elif equipchoice == "3":
			if pickaxe == "Quartz Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Quartz Pickaxe"
				print("Quartz Pickaxe equipped!")
		elif equipchoice == "4":
			if pickaxe == "Quartz and Gold Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Quartz and Gold Pickaxe"
				print("Quartz and Gold Pickaxe equipped!")
		elif equipchoice == "5":
			if pickaxe == "Ancient Debris Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Ancient Debris Pickaxe"
				print("Ancient Debris Pickaxe equipped!")
		elif equipchoice == "6":
			if pickaxe == "Netherite Scrap Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Netherite Scrap Pickaxe"
				print("Netherite Scrap Pickaxe equipped!")
		elif equipchoice == "7":
			if pickaxe == "Netherite Pickaxe":
				print("This pickaxe is already equipped")
			else:
				pickaxe = "Netherite Pickaxe"
				print("Netherite Pickaxe equipped!")
	elif pickaxechecker == 40:
		print("1. Endstone Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Endstone Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "Endstone Pickaxe"
				print("Endstone Pickaxe equipped!")
	elif pickaxechecker == 42:
		print("1. Endstone Pickaxe")
		print("2. End Brick Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Endstone Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "Endstone Pickaxe"
				print("Endstone Pickaxe equipped!")
		if equipchoice == "2":
			if pickaxe == "End Brick Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "End Brick Pickaxe"
				print("End Brick Pickaxe equipped!")
	elif pickaxechecker == 44:
		print("1. Endstone Pickaxe")
		print("2. End Brick Pickaxe")
		print("3. Purpur Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Endstone Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "Endstone Pickaxe"
				print("Endstone Pickaxe equipped!")
		if equipchoice == "2":
			if pickaxe == "End Brick Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "End Brick Pickaxe"
				print("End Brick Pickaxe equipped!")
		if equipchoice == "3":
			if pickaxe == "Purpur Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "Purpur Pickaxe"
				print("Purpur Pickaxe equipped!")
	elif pickaxechecker == 46:
		print("1. Endstone Pickaxe")
		print("2. End Brick Pickaxe")
		print("3. Purpur Pickaxe")
		print("4. Unbreakable Endstone Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Endstone Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "Endstone Pickaxe"
				print("Endstone Pickaxe equipped!")
		if equipchoice == "2":
			if pickaxe == "End Brick Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "End Brick Pickaxe"
				print("End Brick Pickaxe equipped!")
		if equipchoice == "3":
			if pickaxe == "Purpur Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "Purpur Pickaxe"
				print("Purpur Pickaxe equipped!")
		if equipchoice == "4":
			if pickaxe == "Unbreakable Endstone Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "Unbreakable Endstone Pickaxe"
				print("Unbreakable Endstone Pickaxe equipped!")
	elif pickaxechecker == 48 or pickaxechecker == 50:
		print("1. Endstone Pickaxe")
		print("2. End Brick Pickaxe")
		print("3. Purpur Pickaxe")
		print("4. Unbreakable Endstone Pickaxe")
		print("5. Ender Dragon Pickaxe")
		equipchoice = input("Pick a pickaxe to equip: ")
		if equipchoice == "1":
			if pickaxe == "Endstone Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "Endstone Pickaxe"
				print("Endstone Pickaxe equipped!")
		if equipchoice == "2":
			if pickaxe == "End Brick Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "End Brick Pickaxe"
				print("End Brick Pickaxe equipped!")
		if equipchoice == "3":
			if pickaxe == "Purpur Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "Purpur Pickaxe"
				print("Purpur Pickaxe equipped!")
		if equipchoice == "4":
			if pickaxe == "Unbreakable Endstone Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "Unbreakable Endstone Pickaxe"
				print("Unbreakable Endstone Pickaxe equipped!")
		if equipchoice == "5":
			if pickaxe == "Ender Dragon Pickaxe":
				print("This pickaxe is already equipped!")
			else:
				pickaxe = "Ender Dragon Pickaxe"
				print("Ender Dragon Pickaxe equipped!")
	input("Press [enter] to continue")
	return pickaxe,pickaxes