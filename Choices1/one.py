import os
import time
import random

def one(enchantments,pickaxes,pickaxe,inventory,quests,sidequests):
	questchecker = sum(len(l) for l in quests)
	os.system('clear')
	if pickaxe == "Wooden Pickaxe":
		if pickaxes[0][1] <= 0:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					stonegained = random.randint(1, 5)
				if enchantments[2][1] == 0:
					durabilityloss = 1
				pickaxes[0][1] -= durabilityloss
				inventory[0][1] += stonegained
				print("You got", stonegained, "stone but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "Stone Pickaxe":
		if pickaxes[1][1] <= 2:
			print("No more or not enough pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
			if enchantments[0][1] == 0:
				stonegained = random.randint(1, 10)
				coalgained = random.randint(1, 5)
			if enchantments[2][1] == 0:
				durabilityloss = 3
			pickaxes[1][1] -= durabilityloss
			inventory[0][1] += stonegained
			inventory[1][1] += coalgained
			print("You got", stonegained, "stone and", coalgained, "coal but lost",str(durabilityloss), "pickaxe durability!")
			input("Press [enter] to continue")
	elif pickaxe == "Coal Pickaxe":
		if pickaxes[2][1] <= 4:
			print("No more or not enough pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
			if enchantments[0][1] == 0:
				stonegained = random.randint(1, 15)
				coalgained = random.randint(1, 10)
				chaingained = random.randint(1, 5)
			if enchantments[2][1] == 0:
				durabilityloss = 5
			pickaxes[2][1] -= durabilityloss
			inventory[0][1] += stonegained
			inventory[1][1] += coalgained
			inventory[2][1] += chaingained
			print("You got", stonegained, "stone,", coalgained, "coal",chaingained,"chain but lost",str(durabilityloss), "pickaxe durability!")
		input("Press [enter] to continue")
	elif pickaxe == "Chain Pickaxe":
		if pickaxes[3][1] <= 6:
			print("No more or not enough pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
			if enchantments[0][1] == 0:
				stonegained = random.randint(1, 20)
				coalgained = random.randint(1, 15)
				chaingained = random.randint(1, 10)
				brickgained = random.randint(1, 5)
			if enchantments[2][1] == 0:
				durabilityloss = 7
			pickaxes[3][1] -= durabilityloss
			inventory[0][1] += stonegained
			inventory[1][1] += coalgained
			inventory[2][1] += chaingained
			inventory[3][1] += brickgained
			print("You got", stonegained, "stone,", coalgained, "coal",chaingained,"chain and",brickgained,"brick but lost",str(durabilityloss), "pickaxe durability!")
		input("Press [enter] to continue")
	elif pickaxe == "Brick Pickaxe":
		if pickaxes[4][1] <= 9:
			print("No more or not enough pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
			if enchantments[0][1] == 0:
				stonegained = random.randint(1, 25)
				coalgained = random.randint(1, 20)
				chaingained = random.randint(1, 15)
				brickgained = random.randint(1, 10)
				irongained = random.randint(1, 5)
			if enchantments[2][1] == 0:
				durabilityloss = 10
			pickaxes[4][1] -= durabilityloss
			inventory[0][1] += stonegained
			inventory[1][1] += coalgained
			inventory[2][1] += chaingained
			inventory[3][1] += brickgained
			inventory[4][1] += irongained
			print("You got", stonegained, "stone,", coalgained, "coal",chaingained,"chain,",brickgained,"brick and",irongained,"iron but lost",str(durabilityloss), "pickaxe durability!")
		input("Press [enter] to continue")
	elif pickaxe == "Iron Pickaxe":
		if pickaxes[5][1] <= 12:
			print("No more or not enough pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
			if enchantments[0][1] == 0:
				stonegained = random.randint(1, 30)
				coalgained = random.randint(1, 25)
				chaingained = random.randint(1, 20)
				brickgained = random.randint(1, 15)
				irongained = random.randint(1, 10)
				steelgained = random.randint(1, 5)
			if enchantments[2][1] == 0:
				durabilityloss = 13
			pickaxes[5][1] -= durabilityloss
			inventory[0][1] += stonegained
			inventory[1][1] += coalgained
			inventory[2][1] += chaingained
			inventory[3][1] += brickgained
			inventory[4][1] += irongained
			inventory[5][1] += steelgained
			print("You got",stonegained,"stone,",coalgained,"coal",chaingained,"chain,",brickgained,"brick,",irongained,"iron",steelgained,"steel but lost",str(durabilityloss), "pickaxe durability!")
		input("Press [enter] to continue")
	elif pickaxe == "Steel Pickaxe":
		if pickaxes[6][1] <= 14:
			print("No more or not enough pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
			if enchantments[0][1] == 0:
				stonegained = random.randint(1, 35)
				coalgained = random.randint(1, 30)
				chaingained = random.randint(1, 25)
				brickgained = random.randint(1, 20)
				irongained = random.randint(1, 15)
				steelgained = random.randint(1, 10)
				goldgained = random.randint(1, 5)
			if enchantments[2][1] == 0:
				durabilityloss = 15
			pickaxes[6][1] -= durabilityloss
			inventory[0][1] += stonegained
			inventory[1][1] += coalgained
			inventory[2][1] += chaingained
			inventory[3][1] += brickgained
			inventory[4][1] += irongained
			inventory[5][1] += steelgained
			inventory[6][1] += goldgained
			print("You got",stonegained,"stone,",coalgained,"coal",chaingained,"chain,",brickgained,"brick,",irongained,"iron",steelgained,"steel and",goldgained,"gold but lost",str(durabilityloss), "pickaxe durability!")
		input("Press [enter] to continue")
	elif pickaxe == "Gold Pickaxe":
		if pickaxes[7][1] <= 19:
			print("No more or not enough pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
			if enchantments[0][1] == 0:
				stonegained = random.randint(1, 40)
				coalgained = random.randint(1, 35)
				chaingained = random.randint(1, 30)
				brickgained = random.randint(1, 25)
				irongained = random.randint(1, 20)
				steelgained = random.randint(1, 15)
				goldgained = random.randint(1, 10)
				diamondgained = random.randint(1, 5)
			if enchantments[2][1] == 0:
				durabilityloss = 20
			pickaxes[7][1] -= durabilityloss
			inventory[0][1] += stonegained
			inventory[1][1] += coalgained
			inventory[2][1] += chaingained
			inventory[3][1] += brickgained
			inventory[4][1] += irongained
			inventory[5][1] += steelgained
			inventory[6][1] += goldgained
			inventory[7][1] += diamondgained
			print("You got",stonegained,"stone,",coalgained,"coal",chaingained,"chain,",brickgained,"brick,",irongained,"iron",steelgained,"steel,",goldgained,"and,",diamondgained,"diamonds but lost",str(durabilityloss), "pickaxe durability!")
		input("Press [enter] to continue")
	elif pickaxe == "Diamond Pickaxe":
		if pickaxes[8][1] <= 22:
			print("No more or not enough pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
			if enchantments[0][1] == 0:
				stonegained = random.randint(1, 45)
				coalgained = random.randint(1, 40)
				chaingained = random.randint(1, 35)
				brickgained = random.randint(1, 30)
				irongained = random.randint(1, 25)
				steelgained = random.randint(1, 20)
				goldgained = random.randint(1, 15)
				diamondgained = random.randint(1, 10)
				emeraldgained = random.randint(1, 5)
			if enchantments[2][1] == 0:
				durabilityloss = 23
			pickaxes[8][1] -= durabilityloss
			inventory[0][1] += stonegained
			inventory[1][1] += coalgained
			inventory[2][1] += chaingained
			inventory[3][1] += brickgained
			inventory[4][1] += irongained
			inventory[5][1] += steelgained
			inventory[6][1] += goldgained
			inventory[7][1] += diamondgained
			inventory[8][1] += emeraldgained
			print("You got",stonegained,"stone,",coalgained,"coal",chaingained,"chain,",brickgained,"brick,",irongained,"iron",steelgained,"steel,",goldgained,"gold,",diamondgained,"diamonds and,",emeraldgained,"emeralds but lost",str(durabilityloss), "pickaxe durability!")
		input("Press [enter] to continue")
	elif pickaxe == "Emerald Pickaxe":
		if pickaxes[9][1] <= 22:
			print("No more or not enough pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
			if enchantments[0][1] == 0:
				stonegained = random.randint(1, 50)
				coalgained = random.randint(1, 45)
				chaingained = random.randint(1, 40)
				brickgained = random.randint(1, 35)
				irongained = random.randint(1, 30)
				steelgained = random.randint(1, 25)
				goldgained = random.randint(1, 20)
				diamondgained = random.randint(1, 15)
				emeraldgained = random.randint(1, 10)
			if enchantments[2][1] == 0:
				durabilityloss = 23
			pickaxes[8][1] -= durabilityloss
			inventory[0][1] += stonegained
			inventory[1][1] += coalgained
			inventory[2][1] += chaingained
			inventory[3][1] += brickgained
			inventory[4][1] += irongained
			inventory[5][1] += steelgained
			inventory[6][1] += goldgained
			inventory[7][1] += diamondgained
			inventory[8][1] += emeraldgained
			print("You got",stonegained,"stone,",coalgained,"coal",chaingained,"chain,",brickgained,"brick,",irongained,"iron",steelgained,"steel,",goldgained,"gold,",diamondgained,"diamonds and,",emeraldgained,"emeralds but lost",str(durabilityloss), "pickaxe durability!")
		input("Press [enter] to continue")
	elif pickaxe == "Netherrack Pickaxe":
		if pickaxes[11][1] <= 0:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					netherrackgained = random.randint(1,10)
					goldnuggetsgained = random.randint(1, 5)
				if enchantments[2][1] == 0:
					durabilityloss = 1
				pickaxes[11][1] -= durabilityloss
				inventory[9][1] += netherrackgained
				inventory[10][1] += goldnuggetsgained
				print("You got", goldnuggetsgained, "gold nuggets and",netherrackgained,"netherrack but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "Gold nugget Pickaxe":
		if pickaxes[12][1] <= 2:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					netherrackgained = random.randint(1,15)
					goldnuggetsgained = random.randint(1, 10)
					quartzgained = random.randint(1,5)
				if enchantments[2][1] == 0:
					durabilityloss = 3
				pickaxes[12][1] -= durabilityloss
				inventory[9][1] += netherrackgained
				inventory[10][1] += goldnuggetsgained
				inventory[11][1] += quartzgained
				print("You got",quartzgained,"quartz,", goldnuggetsgained, "gold nuggets and",netherrackgained,"netherrack but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "Quartz Pickaxe":
		if pickaxes[13][1] <= 4:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					netherrackgained = random.randint(1,20)
					goldnuggetsgained = random.randint(1, 15)
					quartzgained = random.randint(1,10)
					goldgained = random.randint(1, 5)
				if enchantments[2][1] == 0:
					durabilityloss = 5
				pickaxes[13][1] -= durabilityloss
				inventory[9][1] += netherrackgained
				inventory[10][1] += goldnuggetsgained
				inventory[11][1] += quartzgained
				inventory[12][1] += goldgained
				print("You got",goldgained,"gold,",quartzgained,"quartz,", goldnuggetsgained, "gold nuggets and",netherrackgained,"netherrack but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "Quartz and Gold Pickaxe":
		if pickaxes[14][1] <= 6:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					netherrackgained = random.randint(1, 25)
					goldnuggetsgained = random.randint(1, 20)
					quartzgained = random.randint(1, 15)
					goldgained = random.randint(1, 10)
					ancientdebrisgained = random.randint(1, 5)
				if enchantments[2][1] == 0:
					durabilityloss = 7
				pickaxes[14][1] -= durabilityloss
				inventory[9][1] += netherrackgained
				inventory[10][1] += goldnuggetsgained
				inventory[11][1] += quartzgained
				inventory[12][1] += goldgained
				inventory[13][1] += ancientdebrisgained
				print("You got",ancientdebrisgained,"ancient debris,",goldgained,"gold,",quartzgained,"quartz,", goldnuggetsgained, "gold nuggets and",netherrackgained,"netherrack but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "Ancient Debris Pickaxe":
		if pickaxes[15][1] <= 9:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					netherrackgained = random.randint(1, 30)
					goldnuggetsgained = random.randint(1, 25)
					quartzgained = random.randint(1, 20)
					goldgained = random.randint(1, 15)
					ancientdebrisgained = random.randint(1, 10)
					netheritescrapgained = random.randint(1, 5)
				if enchantments[2][1] == 0:
					durabilityloss = 10
				pickaxes[15][1] -= durabilityloss
				inventory[9][1] += netherrackgained
				inventory[10][1] += goldnuggetsgained
				inventory[11][1] += quartzgained
				inventory[12][1] += goldgained
				inventory[13][1] += ancientdebrisgained
				inventory[14][1] += netheritescrapgained
				print("You got",netheritescrapgained,"netherite scraps,",ancientdebrisgained,"ancient debris,",goldgained,"gold,",quartzgained,"quartz,", goldnuggetsgained, "gold nuggets and",netherrackgained,"netherrack but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "Netherite Scrap Pickaxe":
		if pickaxes[16][1] <= 11:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					netherrackgained = random.randint(1, 35)
					goldnuggetsgained = random.randint(1, 30)
					quartzgained = random.randint(1, 25)
					goldgained = random.randint(1, 20)
					ancientdebrisgained = random.randint(1, 15)
					netheritescrapgained = random.randint(1, 10)
					netheriteingotgained = random.randint(1, 5)
				if enchantments[2][1] == 0:
					durabilityloss = 12
				pickaxes[16][1] -= durabilityloss
				inventory[9][1] += netherrackgained
				inventory[10][1] += goldnuggetsgained
				inventory[11][1] += quartzgained
				inventory[12][1] += goldgained
				inventory[13][1] += ancientdebrisgained
				inventory[14][1] += netheritescrapgained
				inventory[15][1] += netheriteingotgained
				print("You got",netheriteingotgained,"netherite ingots",netheritescrapgained,"netherite scraps,",ancientdebrisgained,"ancient debris,",goldgained,"gold,",quartzgained,"quartz,", goldnuggetsgained, "gold nuggets and",netherrackgained,"netherrack but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "Netherite Pickaxe":
		if pickaxes[17][1] <= 14:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					netherrackgained = random.randint(1, 40)
					goldnuggetsgained = random.randint(1, 35)
					quartzgained = random.randint(1, 30)
					goldgained = random.randint(1, 25)
					ancientdebrisgained = random.randint(1, 20)
					netheritescrapgained = random.randint(1, 15)
					netheriteingotgained = random.randint(1, 10)
				if enchantments[2][1] == 0:
					durabilityloss = 15
				pickaxes[17][1] -= durabilityloss
				inventory[9][1] += netherrackgained
				inventory[10][1] += goldnuggetsgained
				inventory[11][1] += quartzgained
				inventory[12][1] += goldgained
				inventory[13][1] += ancientdebrisgained
				inventory[14][1] += netheritescrapgained
				inventory[15][1] += netheriteingotgained
				print("You got",netheriteingotgained,"netherite ingots,",netheritescrapgained,"netherite scraps,",ancientdebrisgained,"ancient debris,",goldgained,"gold,",quartzgained,"quartz,", goldnuggetsgained, "gold nuggets and",netherrackgained,"netherrack but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "Endstone Pickaxe":
		if pickaxes[19][1] <= 0:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					endstonegained = random.randint(1, 10)
					endbrickgained = random.randint(1, 5)
				if enchantments[2][1] == 0:
					durabilityloss = 1
				pickaxes[19][1] -= durabilityloss
				inventory[16][1] += endstonegained
				inventory[17][1] += endbrickgained
				print("You got",endbrickgained,"endbrick and",endstonegained,"endstone but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "End Brick Pickaxe":
		if pickaxes[20][1] <= 4:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					endstonegained = random.randint(1, 15)
					endbrickgained = random.randint(1, 10)
					purpurgained = random.randint(1, 5)
				if enchantments[2][1] == 0:
					durabilityloss = 5
				pickaxes[20][1] -= durabilityloss
				inventory[16][1] += endstonegained
				inventory[17][1] += endbrickgained
				inventory[18][1] += purpurgained
				print("You got",purpurgained,"purpur,",endbrickgained,"endbrick and",endstonegained,"endstone but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "Purpur Pickaxe":
		if pickaxes[21][1] <= 9:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					endstonegained = random.randint(1, 20)
					endbrickgained = random.randint(1, 15)
					purpurgained = random.randint(1, 10)
					unbreakableendstonegained = random.randint(1, 5)
				if enchantments[2][1] == 0:
					durabilityloss = 10
				pickaxes[21][1] -= durabilityloss
				inventory[16][1] += endstonegained
				inventory[17][1] += endbrickgained
				inventory[18][1] += purpurgained
				inventory[19][1] += unbreakableendstonegained
				print("You got",unbreakableendstonegained,"unbreakable endstone,",purpurgained,"purpur,",endbrickgained,"endbrick and",endstonegained,"endstone but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "Unbreakable Endstone Pickaxe":
		if pickaxes[22][1] <= 14:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					endstonegained = random.randint(1, 25)
					endbrickgained = random.randint(1, 20)
					purpurgained = random.randint(1, 15)
					unbreakableendstonegained = random.randint(1, 10)
					enderdragonpiecesgained = random.randint(1, 5)
				if enchantments[2][1] == 0:
					durabilityloss = 15
				pickaxes[22][1] -= durabilityloss
				inventory[16][1] += endstonegained
				inventory[17][1] += endbrickgained
				inventory[18][1] += purpurgained
				inventory[19][1] += unbreakableendstonegained
				inventory[20][1] += enderdragonpiecesgained
				print("You got",enderdragonpiecesgained,"ender dragon pieces,",unbreakableendstonegained,"unbreakable endstone,",purpurgained,"purpur,",endbrickgained,"endbrick and",endstonegained,"endstone but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "Ender Dragon Pickaxe":
		if pickaxes[23][1] <= 29:
			print("No more pickaxe durability!")
			input("Press [enter] to continue")
		else:
			if enchantments[1][1] == 0:
				for i in range(5, 0, -1):
					print("Mining,", i, "seconds left")
					time.sleep(1)
				if enchantments[0][1] == 0:
					endstonegained = random.randint(1, 30)
					endbrickgained = random.randint(1, 25)
					purpurgained = random.randint(1, 20)
					unbreakableendstonegained = random.randint(1, 15)
					enderdragonpiecesgained = random.randint(1, 10)
				if enchantments[2][1] == 0:
					durabilityloss = 30
				pickaxes[23][1] -= durabilityloss
				inventory[16][1] += endstonegained
				inventory[17][1] += endbrickgained
				inventory[18][1] += purpurgained
				inventory[19][1] += unbreakableendstonegained
				inventory[20][1] += enderdragonpiecesgained
				print("You got",enderdragonpiecesgained,"ender dragon pieces,",unbreakableendstonegained,"unbreakable endstone,",purpurgained,"purpur,",endbrickgained,"endbrick and",endstonegained,"endstone but lost", str(durabilityloss),"pickaxe durability!")
				input("Press [enter] to continue")
	elif pickaxe == "Dirt Pickaxe":
		if enchantments[1][1] == 0:
			for i in range(5, 0, -1):
				print("Mining,", i, "seconds left")
				time.sleep(1)
			if enchantments[0][1] == 0:
				grassgained = random.randint(1, 5)
			inventory[21][1] += grassgained
			print("You got",grassgained,"grass!")
	elif pickaxe == "Grass Pickaxe":
		if enchantments[1][1] == 0:
			for i in range(5, 0, -1):
				print("Mining,", i, "seconds left")
				time.sleep(1)
			if enchantments[0][1] == 0:
				woodgained = random.randint(1, 5)
			inventory[22][1] += grassgained
			print("You got",woodgained,"wood!")
	elif pickaxe == "Wood Pickaxe":
		if enchantments[1][1] == 0:
			for i in range(5, 0, -1):
				print("Mining,", i, "seconds left")
				time.sleep(1)
			if enchantments[0][1] == 0:
				diamondsgained = random.randint(1, 5)
			inventory[23][1] += diamondsgained
			print("You got",diamondsgained,"diamonds!")
	if questchecker == 2:
		if quests[0][1] < 5:
			quests[0][1] += 1
	elif questchecker == 6:
		if quests[2][1] < 5:
			quests[2][1] += 1
	elif questchecker == 10:
		if quests[4][1] < 10:
			quests[4][1] += 1
	elif questchecker == 12:
		if quests[5][1] < 10:
			quests[5][1] += 1
	elif questchecker == 14:
		if quests[6][1] < 30:
			quests[6][1] += 1
	sidequests[0][2] -= 1
	sidequests[1][2] -= 1
	return enchantments,pickaxes,pickaxe,inventory,quests,sidequests