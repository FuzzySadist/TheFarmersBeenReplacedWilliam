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
		