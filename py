def MHP():
	cont = 'y'
	# Variables to calculate %wins during switch and %wins during stay.
	sww,swl,stw,stl = 0,0,0,0
	test = 0
	while cont == 'y':
		test = test + 1
		print 'Round: ', test
		ans = randint(1,3)							#Put the prize behind a door
		# print 'shhhhh.... the cow is in door ', ans				#Commented out to hide the answer
		ch1 = int(raw_input('Which door would you choose? (1 or 2 or 3)')) 	#Choosing a door
		# Placing the goat behind a door not choosen by the user
		if ch1 == 1: op1, op2 = 2,3
		elif ch1 == 2: op1, op2 = 3,1
		elif ch1 == 3: op1, op2 = 1,2
		if ans == op2: goat, nogoat = op1, op2
		elif ans == op1: goat, nogoat = op2, op1
		else:
			open = randint(1,2)
			if open == 1: goat, nogoat = op1, op2
			if open == 2: goat, nogoat = op2, op1
		print 'There is a goat behind door', goat, '. Would you like to change your door to door', nogoat, ' ?(y/n)' # Option to change the door
		choice = raw_input()
		if choice == 'n': ch2 = ch1
		elif choice == 'y': ch2 = nogoat
		# Result of this round
		if ch2 == ans: print 'You have won a Cow!'
		else: print 'You failed to win a Cow :( But you can have the goat!'
		# Calculations
		if choice == 'y' and ch2 == ans: sww += 1
		if choice == 'n' and ch2 == ans: stw += 1
		if choice == 'y' and ch2 != ans: swl += 1
		if choice == 'n' and ch2 != ans: stl += 1
		# Overall result for the Monte Hill Problem
		if sww+swl != 0: print 'Switch and win: ', (sww*100)/(sww+swl), '%'
		if stw+stl != 0: print 'Stay and win: ', (stw*100)/(stw+stl), '%'
		cont = raw_input('Would you like to continue? (y/n): ')
