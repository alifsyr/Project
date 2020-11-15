import modules

def switchcity(currentUser, foundmonster):
	result = modules.randomrange(501)
	if result >= (500 - int(currentUser[8])):
		print("Fast travelling...")
		if currentUser[10] == "1":					# City : Windhelm
			foundmonster = False
			currentUser[10]= "2" 					# Arrive at Solitude
			print("You have arrived at Solitude")

		else :  									# City : Solitude
			foundmonster = False
			currentUser[10]= "1" 					# Arrive at Windhelm
			print("You have arrived at Windhelm")

		return currentUser, foundmonster

	else : 											# choice(switch_city)==2
		print("Fast travelling...")
		print("Oh no you can’t fast travel when enemies are nearby")
		foundmonster = True
		
		return currentUser, foundmonster