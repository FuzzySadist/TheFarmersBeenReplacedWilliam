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
		

def harvest_field():		
	for ewloop in range(get_world_size()):
		for nsloop in range(get_world_size()):	
			if get_water() < 0.1:
				use_item(Items.Water_Tank)
			if can_harvest():
				harvest()	
			move(North)
		move(East)		
				