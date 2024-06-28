maxseeds = get_world_size()*get_world_size()
clear()

loops = 0	
while loops < 100:
	loops = loops + 1
	if num_items(Items.Empty_Tank) < 10:
		trade(Items.Empty_Tank,10)		
	if num_items(Items.Pumpkin_Seed) < maxseeds:
		trade(Items.Pumpkin_Seed, maxseeds)			
	if num_items(Items.Carrot_Seed) < maxseeds:
		trade(Items.Carrot_Seed,maxseeds)			
	if num_items(Items.Sunflower_Seed) < maxseeds:
		trade(Items.Sunflower_Seed,maxseeds)			
	grow_hay(10)			
	grow_wood(5)
	harvest_field()
	grow_pumpkins(5)
	grow_carrots(5)
	grow_sunflowers(5)
						
def grow_pumpkins(howmuch):
	for i in range(howmuch):
		if num_items(Items.Pumpkin_Seed) < maxseeds:
			trade(Items.Pumpkin_Seed, maxseeds)
		needs_tillin()
		for ewloop in range(get_world_size()):
			for nsloop in range(get_world_size()):	
				plant(Entities.Pumpkin)
				move(North)
			move(East)
		wait(1500)
		harvest_field()

def grow_carrots(howmuch):
	for i in range(howmuch):
		if num_items(Items.Carrot_Seed) < maxseeds:
			trade(Items.Carrot_Seed,maxseeds)	
		needs_tillin()
		for ewloop in range(get_world_size()):
			for nsloop in range(get_world_size()):	
				plant(Entities.Carrots)
				move(North)
			move(East)
		wait(1500)
		harvest_field()

def grow_sunflowers(howmuch):
	needs_tillin()
	for i in range(howmuch):
		if num_items(Items.Sunflower_Seed) < maxseeds:
			trade(Items.Sunflower_Seed,maxseeds)	
		for ewloop in range(get_world_size()):
			for nsloop in range(get_world_size()):	
				plant(Entities.Sunflower)
				move(North)
			move(East)
		wait(1500)
		biggest_sunflower()
		#harvest_field()

def grow_wood(howmuch):
	for i in range(howmuch):
		clear()
		for ewloop in range(get_world_size()):
			for nsloop in range(get_world_size()):	
				if ewloop % 2 == 0:
					plant(Entities.Bush)
				elif nsloop % 2 == 0:
					plant(Entities.Bush)
				else:
					plant(Entities.Tree)
				move(North)
			move(East)
		wait(2500)
		harvest_field()		
			
def grow_hay(howmuch):
	for i in range(howmuch):
		clear()
		wait(500)
		harvest_field()

def biggest_sunflower():
	steps = 0
	maxmeasure = 0
	returnstep = 0
	for ewloop in range(get_world_size()):
		for nsloop in range(get_world_size()):	
			steps=steps+1
			if (measure() > maxmeasure):
				maxmeasure=measure()
				returnstep=steps
			move(North)
		move(East)
	steps = 0	
	found = False
	for ewloop in range(get_world_size()):
		for nsloop in range(get_world_size()):	
			steps=steps+1
			if (steps==returnstep):
				harvest()
				found=True
			move(North)
			if found:
				break
		move(East)
		if found:
			break

def needs_tillin():		
	for ewloop in range(get_world_size()):
		for nsloop in range(get_world_size()):	
			if get_entity_type() == Entities.Grass:
				till()
			move(North)
		move(East)
				
def wait(timer):
	waitsec = 0
	while waitsec < timer:
		waitsec = waitsec + 1

def harvest_field():		
	for ewloop in range(get_world_size()):
		for nsloop in range(get_world_size()):	
			if get_water() < 0.1:
				use_item(Items.Water_Tank)
			if can_harvest():
				harvest()	
			move(North)
		move(East)		
