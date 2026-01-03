from __builtins__ import *

def round(number, place):
	divided = number / place
	rounded = (divided + 0.5) // 1
	return rounded * place

# 合計1にする
rate_for_carrot = 2 / 10
rate_for_bush = 3 / 10
rate_for_pumpkin = 3 / 10
rate_for_grass = 2 / 10

rows_for_carrot = round(get_world_size() * rate_for_carrot, 1)
rows_for_bush = round(get_world_size() * rate_for_bush, 1)
rows_for_pumpkin = round(get_world_size() * rate_for_pumpkin, 1)
rows_for_grass = round(get_world_size() * rate_for_grass, 1)


clear()

for i in range(get_world_size()):
	for j in range(get_world_size()):
		if i < rows_for_carrot:
			till()
			plant(Entities.Carrot)
		elif i < rows_for_carrot + rows_for_bush:
			if(get_pos_x() + get_pos_y()) % 2 == 0:
				plant(Entities.Bush)
			else:
				plant(Entities.Tree)
		elif i < rows_for_carrot + rows_for_bush + rows_for_pumpkin:
			till()
			plant(Entities.Pumpkin)
		use_item(Items.Water)
		move(North)
	move(East)

while True:
	for i in range(rows_for_carrot):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
			if get_water() < 0.5:
				use_item(Items.Water)
			if(get_pos_y() + 1 != get_world_size()):
				move(North)
			else:
				move(North)
				move(East)

	for i in range(rows_for_bush):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				if (get_pos_x() + get_pos_y()) % 2 == 0:
					plant(Entities.Bush)
				else:
					plant(Entities.Tree)
			if get_water() < 0.5:
				use_item(Items.Water)
			if(get_pos_y() + 1 != get_world_size()):
				move(North)
			else:
				move(North)
				move(East)

	for i in range(rows_for_pumpkin):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			plant(Entities.Pumpkin)
			if get_water() < 0.5:
				use_item(Items.Water)
			if(get_pos_y() + 1 != get_world_size()):
				move(North)
			else:
				move(North)
				move(East)

	for i in range(rows_for_grass):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				plant(Entities.Grass)
			if get_water() < 0.5:
				use_item(Items.Water)
			if(get_pos_y() + 1 != get_world_size()):
				move(North)
			else:
				move(North)
				move(East)
