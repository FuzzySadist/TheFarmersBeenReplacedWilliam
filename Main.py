maxseeds = get_world_size()*get_world_size()
clear()

loops = 0	
while loops < 100:
	loops = loops + 1
	buy_supplies()		
	
	grow_hay(10)			
	grow_wood(5)
	harvest_field()
	grow_pumpkins(5)
	grow_carrots(5)
	grow_sunflowers(5)
						