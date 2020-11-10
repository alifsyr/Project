import random


def Switch_City(currentUser):
	switch_city=[1,2]
	if random.choice(switch_city)==1:
		print("Fast travelling...")
		if currentUser[10]==1: # City : Windhelm
			currentUser[10]==0 # Arrive at Solitude
			print("You have arrived at "+currentUser[10])
		else :  # City : Solitude
			currentUser[10]==1 # Arrive at Windhelm
			print("You have arrived at "+currentUser[10])
		return currentUser
	else : # choice(switch_city)==2
		print("Fast travelling...")
		print("Oh no you can’t fast travel when enemies are nearby\nYou have met a tundra spider, will you fight or will you flee ( luck * 10% )? ")





	

         


	