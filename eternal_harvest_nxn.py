while True:
	for i in range(get_world_size()):
		if i == 1:
			if can_harvest():
				harvest()
				plant(Entities.Bush)
		elif i == 2:
			if can_harvest():
				harvest()
				till()
				plant(Entities.Carrot)
		else:
			if can_harvest():
				harvest()
				plant(Entities.Grass)
		move(North)
	move(East)