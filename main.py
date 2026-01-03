from __builtins__ import *

def round(number, place):
	divided = number / place
	rounded = (divided + 0.5) // 1
	return rounded * place

# 合計1にする
rate_for_carrot = 3 / 10
rate_for_bush = 3 / 10
rate_for_grass = 4 / 10

rows_for_carrot = round(get_world_size() * rate_for_carrot, 1)
rows_for_bush = round(get_world_size() * rate_for_bush, 1)
rows_for_grass = round(get_world_size() * rate_for_grass, 1)

clear()

for i in range(get_world_size()):
	for j in range(get_world_size()):
		if i < rows_for_carrot:
			till()
			plant(Entities.Carrot)
		elif i < rows_for_carrot + rows_for_bush:
			plant(Entities.Bush)
		move(North)
	move(East)

while True:
	for i in range(rows_for_carrot):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
			if(get_pos_y() + 1 != get_world_size()):
				move(North)
			else:
				move(North)
				move(East)

	for i in range(rows_for_bush):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				plant(Entities.Bush)
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
			if(get_pos_y() + 1 != get_world_size()):
				move(North)
			else:
				move(North)
				move(East)
