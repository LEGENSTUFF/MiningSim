import os
def three(pickaxes,inventory,money,quests):
	os.system("clear")
	pickaxechecker = sum(len(l) for l in pickaxes)
	if pickaxechecker == 2:
		print("1. Stone Pickaxe - $25")
		craftchoice = input("Which pickaxe to craft? ")
		if craftchoice == "1":
			if money >= 25:
				pickaxes.append(["Stone Pickaxe", 131])
				inventory.append(["Coal:",0])
				money = money - 25
				print("You just got the STONE PICKAXE!!!")
				quests[1][1] += 1
				
			else:
				print("Not enough money!")
	elif pickaxechecker == 4:
		print("1. Coal Pickaxe - $75")
		craftchoice = input("Which pickaxe to craft? ")
		if craftchoice == "1":
			if money >= 75:
				pickaxes.append(["Coal Pickaxe",200])
				inventory.append(["Chain:",0])
				money = money - 75
				print("You just got the COAL PICKAXE!!!")
				quests[3][1] += 1
			else:
				print("Not enough money!")
	elif pickaxechecker == 6:
		print("1. Chain Pickaxe - $150")
		craftchoice = input("Which pickaxe to craft? ")
		if craftchoice == "1":
			if money >= 150:
				pickaxes.append(["Chain Pickaxe",250])
				inventory.append(["Brick:",0])
				money = money - 150
				print("You just got the CHAIN PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 8:
		print("1. Brick Pickaxe - $350")
		craftchoice = input("Which pickaxe to craft? ")
		if craftchoice == "1":
			if money >= 350:
				pickaxes.append(["Brick Pickaxe",300])
				inventory.append(["Iron:",0])
				money = money - 350
				print("You just got the BRICK PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 10:
		print("1. Iron Pickaxe - $500")
		craftchoice = input("Which pickaxe to craft? ")
		if craftchoice == "1":
			if money >= 500:
				pickaxes.append(["Iron Pickaxe",350])
				inventory.append(["Steel:",0])
				money = money - 500
				print("You just got the IRON PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 12:
		print("1. Steel Pickaxe - $750")
		craftchoice = input("Which pickaxe to craft? ")
		if craftchoice == "1":
			if money >= 750:
				pickaxes.append(["Steel Pickaxe",400])
				inventory.append(["Gold:",0])
				money = money - 750
				print("You just got the STEEL PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 14:
		print("1. Gold Pickaxe - $1000")
		craftchoice = input("Which pickaxe to craft? ")
		if craftchoice == "1":
			if money >= 1000:
				pickaxes.append(["Gold Pickaxe",500])
				inventory.append(["Diamonds:",0])
				money = money - 1000
				print("You just got the GOLD PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 16:
		print("1. Diamond Pickaxe - $1250")
		craftchoice = input("Which pickaxe to craft? ")
		if craftchoice == "1":
			if money >= 1250:
				pickaxes.append(["Diamond Pickaxe",750])
				inventory.append(["Emeralds:",0])
				money = money - 1250
				print("You just got the DIAMOND PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 18:
		print("1. Emerald Pickaxe - $2500")
		craftchoice = input("Which pickaxe to craft? ")
		if craftchoice == "1":
			if money >= 2500:
				pickaxes.append(["Emerald Pickaxe",1000])
				money = money - 2500
				print("You just got the EMERALD PICKAXE!!!")
				quests[7][1] += 1
			else:
				print("Not enough money!")
	elif pickaxechecker == 20:
		print("1. World 2 Key - $3000")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 3000:
				pickaxes.append(["World 2 Key",1000])
				money = money - 3000
				print("You just got the WORLD 2 KEY!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 24:
		print("1. Gold Nugget Pickaxe - $50")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 50:
				pickaxes.append(["Gold Nugget Pickaxe",250])
				inventory.append(["Quartz:",0])
				money = money - 50
				print("You just got the GOLD NUGGET PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 26:
		print("1. Quartz Pickaxe - $100")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 100:
				pickaxes.append(["Quartz Pickaxe",500])
				inventory.append(["Gold:",0])
				money = money - 100
				print("You just got the QUARTZ PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 28:
		print("1. Quartz and Gold Pickaxe - $250")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 250:
				pickaxes.append(["Quartz and Gold Pickaxe",750])
				inventory.append(["Ancient Debris:",0])
				money = money - 250
				print("You just got the QUARTZ AND GOLD PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 30:
		print("1. Ancient Debris Pickaxe - $350")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 350:
				pickaxes.append(["Ancient Debris Pickaxe",1000])
				inventory.append(["Netherite Scrap:",0])
				money = money - 350
				print("You just got the ANCIENT DEBRIS PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 32:
		print("1. Netherite Scrap Pickaxe - $500")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 500:
				pickaxes.append(["Netherite Scrap Pickaxe",1500])
				inventory.append(["Netherite Ingot:",0])
				money = money - 500
				print("You just got the NETHERITE SCRAP PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 34:
		print("1. Netherite Pickaxe - $600")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 600:
				pickaxes.append(["Netherite Pickaxe",3000])
				money = money - 600
				print("You just got the NETHERITE PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 36:
		print("1. World 3 Key - $1000")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 1000:
				pickaxes.append(["World 3 Key",3000])
				money = money - 1000
				print("You just got the WORLD 3 KEY!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 40:
		print("1. Endbrick Pickaxe - $150")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 150:
				pickaxes.append(["Endbrick Pickaxe",1000])
				inventory.append(["Purpur:",0])
				money = money - 150
				print("You just got the ENDBRICK PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 42:
		print("1. Purpur Pickaxe - $250")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 250:
				pickaxes.append(["Purpur Pickaxe",2500])
				inventory.append(["Unbreakable Endstone:",0])
				money = money - 250
				print("You just got the PURPUR PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 44:
		print("1. Unbreakable Endstone Pickaxe - $500")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 500:
				pickaxes.append(["Endbrick Pickaxe",5000])
				inventory.append(["Ender Dragon Pieces:",0])
				money = money - 500
				print("You just got the UNBREAKABLE ENDSTONE PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 46:
		print("1. Ender Dragon Pickaxe - $1000")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 1000:
				pickaxes.append(["Ender Dragon Pickaxe",10000])
				money = money - 1000
				print("You just got the ENDER DRAGON PICKAXE!!!")
			else:
				print("Not enough money!")
	elif pickaxechecker == 48:
		print("1. Skill Realm + World 4 Key - $1500")
		craftchoice = input("What to craft? ")
		if craftchoice == "1":
			if money >= 1500:
				pickaxes.append(["Skill Realm + World 4 Key",10000])
				money = money - 1500
				print("You just got the SKILL REALM + WORLD 4 KEY!!!")
			else:
				print("Not enough money!")
	else:
		print("New crafts on 15/5/2023")
	input("Press [enter] to continue")
	return pickaxes,inventory,money,quests
