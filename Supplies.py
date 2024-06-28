def buy_supplies():
	if num_items(Items.Empty_Tank) < 10:
		trade(Items.Empty_Tank,10)		
	if num_items(Items.Pumpkin_Seed) < maxseeds:
		trade(Items.Pumpkin_Seed, maxseeds)			
	if num_items(Items.Carrot_Seed) < maxseeds:
		trade(Items.Carrot_Seed,maxseeds)			
	if num_items(Items.Sunflower_Seed) < maxseeds:
		trade(Items.Sunflower_Seed,maxseeds)	