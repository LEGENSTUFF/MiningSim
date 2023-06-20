import time
def six(quests,money,world):
	if world == "World 1":
		if quests[0][1] == 0:
			print("Hey it's me, Tim! I'm your quest guy! I will help you at the start and my requests will get harder and harder. Can you mine 5 times for me?")
			time.sleep(2)
			print("NEW QUEST: MINE 5 TIMES\nREWARD: $5")
		elif quests[0][1] >= 1 and quests[0][1] < 5:
			print("QUEST: MINE",str(5 - quests[0][1]),"MORE TIMES")
		elif quests[0][1] == 5:
			print("Thanks for doing it!")
			print("Please buy the stone pickaxe!")
			quests.append(["Buy the stone pickaxe",0])
			time.sleep(2)
			quests[0][1] += 1
			money += 5
			print("NEW QUEST: CRAFT THE STONE PICKAXE\nREWARD: $10")
		elif quests[1][1] == 0:
			print("QUEST: CRAFT THE STONE PICKAXE")
		elif quests[1][1] == 1:
			print("Thanks for doing it!")
			print("Please mine 5 times and sell 10 stone!")
			quests.append(["Mine 5 times",0,"Sell 10 stone",0])
			time.sleep(2)
			quests[1][1] += 1
			money += 10
			print("NEW QUEST: MINE 5 TIMES AND SELL 10 STONE\nREWARD: $10")
		elif quests[2][1] < 5 or quests[2][3] < 10:
			print("QUEST: MINE",str(5-quests[2][1]),"MORE TIMES AND SELL",str(10-quests[2][3]),"MORE STONE")
		# new not done pts yet
		elif quests[2][1] == 5 and quests[2][3] == 10:
			print("QUEST COMPLETED")
			print("Craft the coal pickaxe!")
			quests.append(["Craft the coal pickaxe",0])
			quests[2][1] += 1
			quests[2][3] +=1
			money += 10
			print("NEW QUEST: CRAFT THE COAL PICKAXE\nREWARD: $15")
		elif quests[3][1] == 0:
			print("QUEST: CRAFT THE COAL PICKAXE\nREWARD: $15")
		elif quests[3][1] == 1:
			print("Thanks!")
			print("Mine 10 times!")
			quests.append(["Mine 10 times",0])
			quests[3][1] += 1
			money += 15
			print("NEW QUEST: MINE 10 TIMES\nREWARD: $150")
		elif quests[4][1] < 10:
			print("QUEST: MINE",str(10-quests[4][1]),"MORE TIMES\nREWARD: $150")
		elif quests[4][1] == 10:
			print("I forgot to tell you just now but please mine 10 more times!")
			quests.append(["Mine 10 times",0])
			quests[4][1] += 1
			money += 150
			print("NEW QUEST: MINE 10 TIMES\nREWARD: $200")
		elif quests[5][1] < 10:
			print("QUEST: MINE",str(10-quests[5][1]),"MORE TIMES\nREWARD:$200")
		elif quests[5][1] == 10:
			print("Mine 30 times!")
			quests.append(["Mine 30 times",0])
			quests[5][1] += 1
			money += 200
			print("NEW QUEST: MINE 10 TIMES\nREWARD: $750")
		elif quests[6][1] < 30:
			print("QUEST: MINE",str(30-quests[6][1]),"MORE TIMES\nREWARD: $750")
		elif quests[6][1] == 30:
			print("Thanks! Please craft the Emerald Pickaxe!")
			quests.append(["Craft the Emerald Pickaxe",0])
			money += 750
			print("NEW QUEST: CRAFT THE EMERALD PICKAXE\nREWARD: $1000")
		elif quests[7][1] == 0:
			print("QUEST: CRAFT THE EMERALD PICKAXE\nREWARD: $1000")
		elif quests[7][1] == 1:
			print("Thanks! I have a friend in the NETHER who needs help! Please go help him!")
			print("NO MORE QUESTS IN WORLD 1")
		elif quests[7][1] == 2:
			print("NO MORE QUESTS IN WORLD 1")
		print("Don't craft the Emerald Pickaxe. Quests will break!")
	input("Press [enter] to continue")
	return quests,money,world
		