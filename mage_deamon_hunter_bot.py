import action_simulator.action_combination as action_combination
import time
import random
import image_comp.object_locator as object_locator

## begin definition ##
base_interval_move = 5 # try to move every interval_move second
base_interval_buff = 180 # try to buff every interval_buff second
base_interval_pee = 60

key_attack = 'space'
key_buff = 'b'
key_movement_skill = 'shift'
class_type = "MAGE"
## endof definition## 

def hunt():

	time.sleep(3)

	while True:
		time_start = time.clock()
		for buff_loop in range(0, 4):
			action_combination.buff(key_buff)
			for move_loop in range(0, 15):
				
				#attack
				action_combination.attack(key_attack, base_interval_move + random.uniform(-5, 5))
				time.sleep(1)
				#move
				if class_type == "MAGE" :
					action_combination.move_with_skill('left', key_movement_skill, 5)
					time.sleep(0.3)
					action_combination.move_with_skill('right', key_movement_skill, 2)
				else :
					action_combination.move('left', 2 + random.uniform(-0.5, 0.5))
					time.sleep(0.3)
					action_combination.move('right', 2 + random.uniform(-0.5, 0.5))
					
				#attack
				action_combination.attack(key_attack, base_interval_move + random.uniform(-5, 5))
				time.sleep(1)
				#move
				if class_type == "MAGE" :
					action_combination.move_with_skill('left', key_movement_skill, 2)
					time.sleep(0.3)
					action_combination.move_with_skill('right', key_movement_skill, 5)
				else :
					action_combination.move('left', 2 + random.uniform(-0.5, 0.5))
					time.sleep(0.3)
					action_combination.move('right', 2 + random.uniform(-0.5, 0.5))	
					
					
			time.sleep(5 + random.uniform(-0.5, 0.5))
			
		action_combination.pee()
		action_combination.pee("XD")
	