import time
import os
import random
import pickle
from os import environ as env
from replit import db
from threading import Thread as thread
import datetime
import pytz
from Choices1.one import one
from Choices1.two import two
from Choices1.three import three
from Choices1.four import four
from Choices1.five import five
from Choices1.six import six
from Choices1.seven import seven
import math
import sys

dsta = True
username = env["REPL_OWNER"]
money = 0
world = "World 1"
if username != "":
	money = 0
	skin = "None"
	skins = [["Default","Common"]]
	sidequests = [["1 Star:","Mine times",5],["2 Stars:","Mine times",20],["3 Stars:","Repair pickaxe durability",50]]
	world = "World 1 (Overworld) - Starter Realm"
	readthroughall = False
	pickaxe = "Wooden Pickaxe"
	stars = 0
	level = 1
	denied = False
	coderedeemed1 = False
	coderedeemed2 = False
	coderedeemed3 = False
	collections = [["a",True]]
	inventory = [['Stone:', 0]]
	pickaxes = [['Wooden Pickaxe', 59]]
	enchantments = [["Fortune", 0], ["Haste", 0], ["Unbreakable", 0]]
	quests = [["Mine 5 times", 0]]
	# print("Downloading data [0/370kb]")
	# time.sleep(0.9)
	# os.system("clear")
	# print("Downloading data [58/370kb]")
	# time.sleep(1.2)
	# os.system("clear")
	# print("Downloading data [280/370kb]")
	# time.sleep(1.2)
	# os.system("clear")
	# print("Downloading data [370/370kb]")
	# time.sleep(0.5)
	os.system("clear")
	print("Welcome to mining simulator (v5.0)")
	print("Have you played before?")
	print("1. Yes")
	print("2. No")
	startchoice2 = input("Choose one: ")
	if startchoice2 == "2":
		username = os.environ['REPL_OWNER']
	elif startchoice2 == "1":
		money = db["money"]
		pickaxe = db["pickaxe"]
		inventory = db["inventory"]
		pickaxes = db["pickaxes"]
		enchantments = db["enchantments"]
		world = db["world"]
		coderedeemed1 = db["coderedeemed1"]
		coderedeemed2 = db["coderedeemed2"]
		coderedeemed3 = db["coderedeemed3"]
		quests = db["quests"]
		stars = db["stars"]
		level = db["level"]
		skin = db["skin"]
		skins = db["skins"]
		sidequests = db["sidequests"]
		collections = db["collections"]
			
	print("Welcome,",username)
	print("1. Tutorial")
	print("2. Game")
	startchoice = input("Choose an option: ")
	if startchoice == "1":
		os.system("clear")
		print("Start mining")
		print("Sell ores that you mined")
		print("Complete Quests")
		print("Get money")
		print("Buy pickaxes")
		print("END OF TUTORIAL")
		input("Press [enter] to end")
	os.system('clear')


def save():
	global dsta
	if True:
		while dsta == True:
			db["money"] = money
			db["pickaxe"] = pickaxe
			db["inventory"] = inventory
			db["pickaxes"] = pickaxes
			db["enchantments"] = enchantments
			db["world"] = world
			db["coderedeemed1"] = coderedeemed1
			db["coderedeemed2"] = coderedeemed2
			db["coderedeemed3"] = coderedeemed3
			db["quests"] = quests
			db["stars"] = stars
			db["level"] = level
			db["skin"] = skin
			db["skins"] = skins
			db["sidequests"] = sidequests
			db["collections"] = collections


while True:
	# if username != "MiningSim-Dev-Team":
	# 	break
	# if username == "":
	# 	print("You have been temporarily banned!")
	# 	print("Ban lifts: 23rd April 2023")
	# 	quit()
	pickaxechecker = sum(len(l) for l in pickaxes)
	# 24 is netherrack 26 is gold nugget 28 is quartz 30 is quartz and gold 32 is ancient debris 34 is netherite scrap 36 is netherite 38 is key 40 is endstone(pickaxe 20 in the list is [19])
	os.system('clear')
	print("Main Menu")
	if world != "World 4 (Noob World) - Skill Realm"
	print("Money: $" + str(money))
	print("Skin:",skin)
	if quests[0][1] < 5:
		times = 5 - quests[0][1]
		print("QUEST: MINE",times,"MORE TIMES - $10")
	elif quests[0][1] == 5:
		print("Talk to Tim!")
	elif quests[1][1] == 0:
		print("QUEST: CRAFT THE STONE PICKAXE - $10")
	elif quests[1][1] == 1:
		print("Talk to Tim!")
	elif quests[2][1] < 5 or quests[2][3] < 10:
		print("QUEST: MINE",str(5-quests[2][1]),"MORE TIMES AND SELL",str(10-quests[2][3]),"MORE STONE")
	elif quests[2][1] == 5 and quests[2][3] == 10:
		print("Talk to Tim!")
	elif quests[3][1] == 0:
		print("QUEST: CRAFT THE COAL PICKAXE! - $15")
	elif quests[3][1] == 1:
		print("Talk to Tim!")
	elif quests[4][1] < 10:
		print("QUEST: MINE",str(10-quests[4][1]),"MORE TIMES\nREWARD: $150")
	elif quests[4][1] == 10:
		print("Talk to Tim!")
	elif quests[5][1] < 10:
		print("QUEST: MINE",str(10-quests[5][1]),"MORE TIMES\nREWARD: $200")
	elif quests[5][1] == 10:
		print("Talk to Tim!")
	elif quests[6][1] < 30:
		print("QUEST: MINE",str(30-quests[6][1]),"MORE TIMES\nREWARD: $750")
	elif quests[6][1] == 30:
		print("Talk to Tim!")
	elif quests[7][1] < 1:
		print("QUEST: CRAFT THE EMERALD PICKAXE")
	elif quests[7][1] == 1:
		print("Talk to Tim!")
	elif quests[7][1] == 2:
		if world == "World 1":
			print("NO MORE QUESTS IN WORLD 1!")
	
	print("World:",world)

	if username == "MiningSim-Dev-Team":
		print("---------------------------------------------")
		
		print("Side Quests:")
		if sidequests[0][2] == 0:
			sidequests[0][2] = random.randint(5,10)
			stars += 1
		if sidequests[1][2] == 0:
			sidequests[1][2] = random.randint(20,30)
			stars += 2
		if sidequests[2][2] < 0:
			sidequests[2][2] = random.randint(50,500)
			stars += 3
		print(sidequests[0][0],"Mine",sidequests[0][2],"more times!")
		print(sidequests[1][0],"Mine",sidequests[1][2],"more times!")
		print(sidequests[2][0],"Repair",sidequests[2][2],"more pickaxe durability!")
		print("Stars:",stars)
	print("---------------------------------------------")
	print("Pickaxe Info:")
	print("Pickaxe:", pickaxe)
	if pickaxe == "Wooden Pickaxe":
		print("Pickaxe durability:", pickaxes[0][1])
	elif pickaxe == "Stone Pickaxe":
		print("Pickaxe durability:", pickaxes[1][1])
	elif pickaxe == "Coal Pickaxe":
		print("Pickaxe durability:", pickaxes[2][1])
	elif pickaxe == "Chain Pickaxe":
		print("Pickaxe durability:", pickaxes[3][1])
	elif pickaxe == "Brick Pickaxe":
		print("Pickaxe durability:", pickaxes[4][1])
	elif pickaxe == "Iron Pickaxe":
		print("Pickaxe durability:", pickaxes[5][1])
	elif pickaxe == "Steel Pickaxe":
		print("Pickaxe durability:", pickaxes[6][1])
	elif pickaxe == "Gold Pickaxe":
		print("Pickaxe durability:", pickaxes[7][1])
	elif pickaxe == "Diamond Pickaxe":
		print("Pickaxe durability:", pickaxes[8][1])
	elif pickaxe == "Emerald Pickaxe":
		print("Pickaxe durability:", pickaxes[9][1])
	elif pickaxe == "Netherrack Pickaxe":
		print("Pickaxe durability:", pickaxes[11][1])
	elif pickaxe == "Gold nugget Pickaxe":
		print("Pickaxe durability:", pickaxes[12][1])
	elif pickaxe == "Quartz Pickaxe":
		print("Pickaxe durability:", pickaxes[13][1])
	elif pickaxe == "Quartz and Gold Pickaxe":
		print("Pickaxe durability:", pickaxes[14][1])
	elif pickaxe == "Ancient Debris Pickaxe":
		print("Pickaxe durability:", pickaxes[15][1])
	elif pickaxe == "Netherite Scrap Pickaxe":
		print("Pickaxe durability:", pickaxes[16][1])
	elif pickaxe == "Netherite Pickaxe":
		print("Pickaxe durability:", pickaxes[17][1])
	elif pickaxe == "Endstone Pickaxe":
		print("Pickaxe durability:", pickaxes[19][1])
	elif pickaxe == "End Brick Pickaxe":
		print("Pickaxe durability:", pickaxes[20][1])
	elif pickaxe == "Purpur Pickaxe":
		print("Pickaxe durability:", pickaxes[21][1])
	elif pickaxe == "Unbreakable Endstone Pickaxe":
		print("Pickaxe durability:", pickaxes[22][1])
	elif pickaxe == "Ender Dragon Pickaxe":
		print("Pickaxe durability:", pickaxes[23][1])
	print("--------------------------------------------------------")
	if pickaxechecker == 2:
		print("Inventory:")
		print(inventory[0][0], inventory[0][1])
	elif pickaxechecker == 4:
		print("Inventory:")
		print(inventory[0][0], inventory[0][1])
		print(inventory[1][0], inventory[1][1])
	elif pickaxechecker == 6:
		print("Inventory:")
		print(inventory[0][0], inventory[0][1])
		print(inventory[1][0], inventory[1][1])
		print(inventory[2][0], inventory[2][1])
	elif pickaxechecker == 8:
		print("Inventory:")
		print(inventory[0][0], inventory[0][1])
		print(inventory[1][0], inventory[1][1])
		print(inventory[2][0], inventory[2][1])
		print(inventory[3][0], inventory[3][1])
	elif pickaxechecker == 10:
		print("Inventory:")
		print(inventory[0][0], inventory[0][1])
		print(inventory[1][0], inventory[1][1])
		print(inventory[2][0], inventory[2][1])
		print(inventory[3][0], inventory[3][1])
		print(inventory[4][0], inventory[4][1])
	elif pickaxechecker == 12:
		print("Inventory:")
		print(inventory[0][0], inventory[0][1])
		print(inventory[1][0], inventory[1][1])
		print(inventory[2][0], inventory[2][1])
		print(inventory[3][0], inventory[3][1])
		print(inventory[4][0], inventory[4][1])
		print(inventory[5][0], inventory[5][1])
	elif pickaxechecker == 14:
		print("Inventory:")
		print(inventory[0][0], inventory[0][1])
		print(inventory[1][0], inventory[1][1])
		print(inventory[2][0], inventory[2][1])
		print(inventory[3][0], inventory[3][1])
		print(inventory[4][0], inventory[4][1])
		print(inventory[5][0], inventory[5][1])
		print(inventory[6][0], inventory[6][1])
	elif pickaxechecker == 16:
		print("Inventory:")
		print(inventory[0][0], inventory[0][1])
		print(inventory[1][0], inventory[1][1])
		print(inventory[2][0], inventory[2][1])
		print(inventory[3][0], inventory[3][1])
		print(inventory[4][0], inventory[4][1])
		print(inventory[5][0], inventory[5][1])
		print(inventory[6][0], inventory[6][1])
		print(inventory[7][0], inventory[7][1])
	elif pickaxechecker == 18 or pickaxechecker == 20 or pickaxechecker == 22:
		print("Inventory:")
		print(inventory[0][0], inventory[0][1])
		print(inventory[1][0], inventory[1][1])
		print(inventory[2][0], inventory[2][1])
		print(inventory[3][0], inventory[3][1])
		print(inventory[4][0], inventory[4][1])
		print(inventory[5][0], inventory[5][1])
		print(inventory[6][0], inventory[6][1])
		print(inventory[7][0], inventory[7][1])
		print(inventory[8][0], inventory[8][1])
	elif pickaxechecker == 24:
		print("Inventory:")
		print(inventory[9][0], inventory[9][1])
		print(inventory[10][0], inventory[10][1])
	elif pickaxechecker == 26:
		print("Inventory:")
		print(inventory[9][0], inventory[9][1])
		print(inventory[10][0], inventory[10][1])
		print(inventory[11][0], inventory[11][1])
	elif pickaxechecker == 28:
		print("Inventory:")
		print(inventory[9][0], inventory[9][1])
		print(inventory[10][0], inventory[10][1])
		print(inventory[11][0], inventory[11][1])
		print(inventory[12][0], inventory[12][1])
	elif pickaxechecker == 30:
		print("Inventory:")
		print(inventory[9][0], inventory[9][1])
		print(inventory[10][0], inventory[10][1])
		print(inventory[11][0], inventory[11][1])
		print(inventory[12][0], inventory[12][1])
		print(inventory[13][0], inventory[13][1])
	elif pickaxechecker == 32:
		print("Inventory:")
		print(inventory[9][0], inventory[9][1])
		print(inventory[10][0], inventory[10][1])
		print(inventory[11][0], inventory[11][1])
		print(inventory[12][0], inventory[12][1])
		print(inventory[13][0], inventory[13][1])
		print(inventory[14][0], inventory[14][1])
	elif pickaxechecker == 34 or pickaxechecker == 36 or pickaxechecker == 38:
		print("Inventory:")
		print(inventory[9][0], inventory[9][1])
		print(inventory[10][0], inventory[10][1])
		print(inventory[11][0], inventory[11][1])
		print(inventory[12][0], inventory[12][1])
		print(inventory[13][0], inventory[13][1])
		print(inventory[14][0], inventory[14][1])
		print(inventory[15][0], inventory[15][1])
	elif pickaxechecker == 40:
		print(inventory[16][0], inventory[16][1])
		print(inventory[17][0], inventory[17][1])
	elif pickaxechecker == 42:
		print(inventory[16][0], inventory[16][1])
		print(inventory[17][0], inventory[17][1])
		print(inventory[18][0], inventory[18][1])
	elif pickaxechecker == 44:
		print(inventory[16][0], inventory[16][1])
		print(inventory[17][0], inventory[17][1])
		print(inventory[18][0], inventory[18][1])
		print(inventory[19][0], inventory[19][1])
	elif pickaxechecker == 46 or pickaxechecker == 48 or pickaxechecker == 50:
		print(inventory[16][0], inventory[16][1])
		print(inventory[17][0], inventory[17][1])
		print(inventory[18][0], inventory[18][1])
		print(inventory[19][0], inventory[19][1])
		print(inventory[20][0], inventory[20][1])
	elif pickaxechecker == 52: #grass
		print(inventory[21][0], inventory[21][1])
	elif pickaxechecker == 54: #wood
		print(inventory[21][0], inventory[21][1])
	elif pickaxechecker == 56: #diamonds
		print(inventory[21][0], inventory[21][1])
	print("--------------------------------------------------------")
	print("(!)OPTIONS 1, 2 and 3 DISALBLED FOR WORLDS 4,5 AND 6(!)")
	print("ALWAYS TALK TO TIM IMMEDIATELY ONCE YOU HAVE COMPLETED A QUEST! YOUR GAME WILL BREAK IF YOU DON'T!")
	print("A. Exclusive Egg 1 - $1000")
	print("1. Mine")
	print("2. Sell")
	print("3. Craft")
	print("4. Equip")
	print("5. Repair")
	print("6. Links")
	print("7. Quests")
	print("8. Season Pass")
	print("9. Skins")
	print("10. Save & Exit (Will bring you to the update in how many days page)")
	if pickaxechecker == 22:
		print("11. USE WORLD 2 KEY")
	elif pickaxechecker == 38:
		print("11. USE WORLD 3 KEY")
	elif pickaxechecker == 50:
		print("11. USE WORLD 4 KEY")
	else:
		if readthroughall == False:
			print("11. Newsfeeds (!)")
		else:
			print("11. Newsfeeds")
	print("12. Command Panel")
	choice = input("Choose an option: ")
	if choice == "A" and money >= 1000:
		print("You will be able to sell skins in the future, and some inflation might happen 👀")
		print("50% -> $100")
		print("20% -> $250")
		print("10% -> $500")
		print("8% -> $1000")
		print("7% -> $1500")
		print("4% -> Floppa")
		print("1% -> Sleipnir")
		choice = input("Do it? (Y/N) ")
		if choice == "Y":
			money -= 1000
			chance = random.random()
			if chance <= 0.5:
				print("You got $100! (-90%)")
				money += 100
			elif chance <= 0.7:
				print("You got $250! (-75%)")
				money += 250
			elif chance <= 0.8:
				print("You got $500! (-50%)")
				money += 500
			elif chance <= 0.88:
				print("You got $1000 (+0%)")
				money += 1000
			elif chance <= 0.95:
				print("You got $1500 (+50%)")
				money += 1500
			elif chance <= 0.9899999999:
				print("You got the 'Floppa' skin! (Exclusive)")
				skins.append(["Floppa","Exclusive"])
			elif chance <= 1:
				print("YOU GOT THE 'SLEIPNIR' SKIN! (Exclusive)")
				skins.append(["Sleipnir","Exclusive"])
	if choice == "1":
		enchantments,pickaxes,pickaxe,inventory,quests,sidequests = one(enchantments,pickaxes,pickaxe,inventory,quests,sidequests)
		pass
	elif choice == "2":
		pickaxes,pickaxe,inventory,money,enchantments = two(pickaxes,pickaxe,inventory,money,enchantments)
		pass
	elif choice == "3":
		pickaxes, inventory, money,quests,pickaxe = three(pickaxes,inventory,money,quests,pickaxe)
		pass
	elif choice == "4":
		pickaxe,pickaxes = four(pickaxe,pickaxes)
		pass
	elif choice == "5":
		pickaxe,pickaxes,money = five(pickaxe,pickaxes,money)
		pass
	elif choice == "6":
		os.system("clear")
		print("WE ARE HIRING! \nhttps://forms.gle/LgGFPJDuPKRdzPco9")
		print("OUR WEBSITE! \nhttps://miningsim.weebly.com/")
		print("OUR TWITTER! \nhttps://twitter.com/MiningSimUpd")
		print("OUR DISCORD AND OWNERS YOUTUBE DISCORD! \nhttps://discord.gg/DRXRtx6RXk")
		input("Press [enter] to continue!")
	elif choice == "7":
		quests,money,world = six(quests,money,world)
	elif choice == "8":
		stars,level,skins = seven(stars,level,skins)
	elif choice == "10":
		s = thread(target=save)
		s.start()
		dsta = False
		break
	elif choice == "9":
		for i in range(len(skins)):
			print(skins[(i)][0]+": "+skins[(i)][1])
		skin = input("Choose a skin (1st skin = 1, 2nd skin = 2...): ")
		print("Skin equipped!")
		skin = skins[int(skin)-1][0]
	elif choice == "11" and pickaxechecker == 22:
		print("Are you sure? This resets all your money and pickaxes!\n1. Yes\n2. No")
		choice = input("Choose an option: ")
		if choice == "1":
			for i in range(5, 0, -1):
				print("Rebirthing... ("+str(i)+")")
				time.sleep(1)
			print("Rebirthed!")
			print("Wait... something is happening!")
			beginningstring0 = "AHHHHHHHHHHH"
			for char0 in beginningstring0:
				sys.stdout.write(char0)
				sys.stdout.flush()
				time.sleep(.222)
			print("Loading... Loading...")
			time.sleep(2)
			overworldbosshealth = 100
			health = 100
			bunnyturn = False
			while True:
				if bunnyturn == False:
					if health > 0:
						print("You attack!")
						damage = random.randint(1,10)
						overworldbosshealth -= damage
						print("You did",damage,"damage to the Overworld Boss!")
						print("Health:",health)
						print("Overworld Boss Health:",overworldbosshealth)
						input("Press enter to continue")
						bunnyturn = True
					else:
						print("No more health!")
						print("You lose!")
				elif bunnyturn == True:
					if overworldbosshealth > 0:
						print("Overworld Boss attacks!")
						damage = random.randint(1,10)
						health -= damage
						print("Overworld Boss did",damage,"damage to you!")
						print("Health:",health)
						print("Overworld Boss Health:",overworldbosshealth)
						input("Press enter to continue")
						bunnyturn = False
					if overworldbosshealth <= 0:
						print("Overworld Boss has no more health!\n")
						break
			pickaxe = "Netherrack Pickaxe"
			pickaxes.append(["Netherrack Pickaxe",100])
			world = "World 2 (Nether Realm) - Starter Realm"
			money = 0
			inventory.append(["Netherrack:",0])
			inventory.append(["Gold Nuggets:",0])
	elif choice == "11" and pickaxechecker == 38:
		print("Are you sure? This resets all your money and pickaxes!\n1. Yes\n2. No")
		choice = input("Choose an option: ")
		if choice == "1":
			for i in range(5, 0, -1):
				print("Rebirthing... ("+str(i)+")")
				time.sleep(1)
			print("Rebirthed!")
			print("Wait... something is happening!")
			beginningstring0 = "AHHHHHHHHHHH"
			for char0 in beginningstring0:
				sys.stdout.write(char0)
				sys.stdout.flush()
				time.sleep(.222)
			print("Loading... Loading...")
			time.sleep(2)
			netherbosshealth = 100
			health = 100
			bunnyturn = False
			while True:
				if bunnyturn == False:
					if health > 0:
						print("You attack!")
						damage = random.randint(1,10)
						netherbosshealth -= damage
						print("You did",damage,"damage to the Nether Boss!")
						print("Health:",health)
						print("Nether Boss Health:",netherbosshealth)
						input("Press enter to continue")
						bunnyturn = True
					else:
						print("No more health!")
						print("You lose!")
				elif bunnyturn == True:
					if netherbosshealth > 0:
						print("Nether Boss attacks!")
						damage = random.randint(1,10)
						health -= damage
						print("Nether Boss did",damage,"damage to you!")
						print("Health:",health)
						print("Nether Boss Health:",netherbosshealth)
						input("Press enter to continue")
						bunnyturn = False
					if netherbosshealth < 0:
						print("Nether Boss has no more health!\n")
						break
			pickaxe = "Endstone Pickaxe"
			pickaxes.append(["Endstone Pickaxe",500])
			world = "World 3 (End World) - Starter Realm"
			money = 0
			inventory.append(["Endstone:",0])
			inventory.append(["End Brick:",0])
	elif choice == "11" and pickaxechecker == 50:
		print("Are you sure? This resets all your money and pickaxes!\n1. Yes\n2. No")
		choice = input("Choose an option: ")
		if choice == "1":
			for i in range(5, 0, -1):
				print("Rebirthing... ("+str(i)+")")
				time.sleep(1)
			print("Rebirthed!")
			print("Wait... something is happening!")
			beginningstring0 = "AHHHHHHHHHHH"
			for char0 in beginningstring0:
				sys.stdout.write(char0)
				sys.stdout.flush()
				time.sleep(.222)
			print("The SKILL GUARDIAN comes out of nowhere!")
			time.sleep(2)
			print("He does not allow you to pass... You resort to violence")
			time.sleep(2)
			skillguardhealth = 100
			health = 100
			bunnyturn = False
			while True:
				if bunnyturn == False:
					if health > 0:
						print("You attack!")
						damage = random.randint(1,10)
						skillguardhealth -= damage
						print("You did",damage,"damage to the Skill Guardian!")
						print("Health:",health)
						print("Skill Guardian Health:",skillguardhealth)
						input("Press enter to continue")
						bunnyturn = True
					else:
						print("No more health!")
						print("You lose!")
				elif bunnyturn == True:
					if skillguardhealth > 0:
						print("Skill Guardian attacks!")
						damage = random.randint(1,10)
						health -= damage
						print("Skill Guardian did",damage,"damage to you!")
						print("Health:",health)
						print("Skill Guardian Health:",skillguardhealth)
						input("Press enter to continue")
						bunnyturn = False
					if skillguardhealth < 0:
						print("Skill Guardian has no more health!\n")
						break
			pickaxe = "Dirt Pickaxe"
			pickaxes.append(["Dirt Pickaxe",25])
			world = "World 4 (Noob World) - Skill Realm"
			money = 0
			inventory.append(["Grass:",0])
	elif choice == "11":
		os.system("clear")
		print("BRAND NEW UPDATE WITH A SEASON!")
		print("1/1")
		print("1. Next")
		print("2. Exit")
		readthroughall = True
		choice = input("Enter your choice: ")
		if choice == "1":
			os.system("clear")
			print("No new newsfeeds!")
		input("Press [enter] to continue")
	elif choice == "12":
		print("COMMAND PANEL")
		if username != "MiningSim-Dev-Team":
			print("Normal:")
			print("You don't have access to this!")
			print("1. Give _______")
			print("2. Give ___________")
			print("3. View ______")
			print("4. Complete ______")
			print("5. View ______ and ______")
		elif username == "MiningSim-Dev-Team":
			print("Owner:")
			print("1. Give self $10000")
			print("2. Give self next pickaxe")
			print("3. View quests")
			print("4. Complete quest")
			print("5. View stars and levels")
			print("6. 10k stars")
			choice = input("choose:")
			if choice == "1":
				money += 10000
			elif choice == "2":
				pickaxes.append(["Admin",100000000000])
				inventory.append(["Admin",100000000000000000])
			elif choice == "3":
				quests,money,world = six(quests,money,world)
			elif choice == "4":
				if quests[0][1] < 5:
					quests[0][1] = 5
				elif quests[1][1] < 1:
					quests[1][1] = 1
				elif quests[2][1] < 5 or quests[2][3] < 10:
					quests[2][1] = 5
					quests[2][3] = 10
				elif quests[3][1] == 0:
					quests[3][1] = 1
				elif quests[4][1] < 10:
					quests[4][1] = 10
				elif quests[5][1] < 10:
					quests[5][1] = 10
				elif quests[6][1] < 30:
					quests[6][1] = 30
				elif quests[7][1] == 0:
					quests[7][1] = 1
			elif choice == "5":
				stars,level,skins = seven(stars,level,skins)
			elif choice == "6":
				stars += 10000
				
		input("Press [enter] to continue")
	elif choice == "v2!" and coderedeemed1 == False:
		money += 1000
		print("You got $1000")
		input("Press [enter] to continue")
		coderedeemed1 = True
	elif choice == "v2!" and coderedeemed1 == True:
		print("Redeemed already")
		input("Press [enter] to continue")
	elif choice == "really early" and coderedeemed2 == False:
		money += 1000
		print("You got $1000")
		input("Press [enter] to continue")
		coderedeemed2 = True
	elif choice == "really early" and coderedeemed2 == True:
		print("Redeemed already")
		input("Press [enter] to continue")
	elif choice == "really early again" and coderedeemed3 == False:
		money += 2000
		print("You got $2000")
		input("Press [enter] to continue")
		coderedeemed3 = True
	elif choice == "really early again" and coderedeemed3 == True:
		print("Redeemed already")
		input("Press [enter] to continue")
	if pickaxechecker == 50 and denied == False:
		os.system("clear")
		print("Psst!")
		time.sleep(1)
		print("My name is Tim!")
		time.sleep(1)
		print("Want to sell me your soul?")
		time.sleep(1)
		print("1. Yes")
		print("2. No")
		endchoice = input("Yes or no: ")
		if endchoice == "1":
			print("You have sold your soul to Tim!!!")
			print("______       ______")
			print("|    |       |    |")
			print("|    |       |    |")
			print("------       ------")
			print("|    |       |    |")
			print("\    \       /    /")
			print(" \    \     /    /")
			print("  \    \   /    /")
			print("------------------")
			print("|                |")
			print("|                |")
			print("------------------")
			print("Thanks for playing!")
			money = 0
			pickaxes = [["Wooden Pickaxe",59]]
			world = "World 1"
			inventory = [["Stone:",0]]
			s = thread(target=save)
			s.start()
			dsta = False
			break
		else:
			denied = True
			pass
update = False
while update == False:
	
	dt = datetime.datetime.now()
	# print("Downtime for v5.0 is live now!")
	# mont = dt.month
	# hour = dt.hour
	# mon=4-dt.month
	# day=27-dt.day
	# if day <= 0:
	# 	if mont == 1 or mont == 3 or mont == 5 or mont == 7 or mont == 8 or mont == 10 or mont == 12:
	# 		day += 31
	# 	elif mont == 2:
	# 		day += 28
	# 	else:
	# 		day += 30
	# 	mon -= 1
	# hr=10-dt.hour
	# if hr < 0:
	# 	day -= 1
	# 	hr += 24
	# mn=60-dt.minute
	# sec=60-dt.second
	# print("Next update in",day,"days,",hr,"hours,",mn, "minutes and", sec,
	#       "seconds")
	# print("Next update soon!")
	print("Previous update:")
	print("v5.0 - Season Pass Update\n")
	print("Next update:")
	print("v5.1 - Noob Update\n")
	mont = dt.month
	mon=6-dt.month
	day=29-dt.day
	if day < 0:
		if mont == 1 or mont == 3 or mont == 5 or mont == 7 or mont == 8 or mont == 10 or mont == 12:
			day += 31
		elif mont == 2:
			day += 28
		else:
			day += 30
		mon -= 1
	hr=11-dt.hour
	if hr < 0:
		day -= 1
		hr += 24
	mn=60-dt.minute
	sec=60-dt.second
	print("Next update in",mon,"months,", day, "days,", hr, "hours,", mn, "minutes and", sec,
	      "seconds\n")
	# print("Downtime ends in",mon,"months,", day, "days,", hr, "hours,", mn, "minutes and", sec,
	#       "seconds")
	mont = dt.month
	mon=7-dt.month
	day=18-dt.day
	if day <= 0:
		if mont == 1 or mont == 3 or mont == 5 or mont == 7 or mont == 8 or mont == 10 or mont == 12:
			day += 31
		elif mont == 2:
			day += 28
		else:
			day += 30
		mon -= 1
	hr=9-dt.hour
	if hr < 0:
		day -= 1
		hr += 24
	mn=60-dt.minute
	sec=60-dt.second
	print("Next season in",mon,"months,", day, "days,", hr, "hours,", mn, "minutes and", sec,"seconds")
	time.sleep(1)
	os.system("clear")
	
	
	# if day == 0 and hr == 0 and mn == 0 and sec == 0:
	# 	os.system("clear")
	# 	update = True
	# else:
	# 	pass
	
print("The update will come soon")
quit()
