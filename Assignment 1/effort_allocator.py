#This work is based on the work of Ash Tyndall (ash.id.au),developed as part of CITS5502 Software Process at the School of Computer Science and Software Engineering, The University of Western Australia. A copy of this can be found at https://github.com/atyndall/cits5502/blob/master/assignment2/scripts/effort-allocator-fifo.py

import random

DATA = [
	[10,5,8,25],
	[7,10,6,19],
	[6,5,5,16],
	[7,4,8,8],
	[2,5,2,14],
	[3,3,1,16],
	[1,2,1,15],
	[3,1,3,9],
	[1,4,1,7],
	[0,2,3,5],
	[1,1,1,5],
	[2,0,3,2],
	[2,1,2,2],
	[2,1,3,2],
	[1,1,0,1],
	[0,0,1,1],
	[2,2,0,0],
	[0,1,0,1],
	[1,2,0,1],
	[0,0,1,0],
]


PRIORITY = [
	2, # Hard & Major
	4, # Hard & Minor
	1, # Easy & Major
	3, # Easy & Minor
]

HOURS_TO_FIX = [
	5, # Hard & Major
	5, # Hard & Minor
	2, # Easy & Major
	2, # Easy & Minor
]

WORK_WEEK = 25

EMPLOYEES = 3

#REPAIRERS = [2] * len(DATA_SET) # random allocation
REPAIRERS = [
	1,
	1,
	1,
	1,
	2,
	2,
	2,
	2,
	2,
	2,
	2,
	2,
	2,
	2,
	2,
	2,
	3,
	3,
	3,
	3,			
]

if __name__ == "__main__":
	fix_list = []
	cumulative = [0, 0, 0, 0]
	
	prior = list(enumerate(PRIORITY))
	prior = sorted(prior, key=lambda x: x[1])

	for week in range(len(DATA)):
		repairers = EMPLOYEES - REPAIRERS[week]
		hours_remaining = WORK_WEEK * REPAIRERS[week]
		
		found = [0, 0, 0, 0]
		w_count = week
		if repairers > 0:
			for i in range(repairers):
				found = [x+y for x, y in zip(found, DATA[w_count])]
				w_count += 1
				if w_count >= len(DATA):
					break
				if i > 0:
					del DATA[w_count]
					DATA.append([0] * 4)
		else:
			DATA.insert(week, [0] * 4)
			del DATA[-1]
			
		bugs_remaining = [x+y for x, y in zip(found, cumulative)]
	
		week_fix = [0, 0, 0, 0]
		#random
		#exhausted = [False, False, False, False]
		
		#random
		#while hours_remaining >= min(HOURS_TO_FIX):
			#type = random.randint(0, 3)
			
			#if bugs_remaining[type] > 0 and hours_remaining >= HOURS_TO_FIX[type]:
				#hours_remaining -= HOURS_TO_FIX[type]
				#bugs_remaining[type] -= 1
				#week_fix[type] += 1
			#else:
				#exhausted[type] = True
				#if all(exhausted):
					#break
		
		#first in first out
		#or i in range(len(cumulative)):
			#for typer, _ in prior:
				#week_bugs = cumulative[i]
				#remaining_bugs = week_bugs[typer]
				
				#if remaining_bugs == 0:
					#continue
				
				#max_bugs = hours_remaining // HOURS_TO_FIX[typer]
			
				#to_fix = min(remaining_bugs, max_bugs)
			
				#week_fix[typer] += to_fix
				
				#hours_remaining -= to_fix * HOURS_TO_FIX[typer]
				#cumulative[i][typer] -= to_fix
	
	
		for type, _ in prior:
			remaining_bugs = bugs_remaining[type]
			max_bugs = hours_remaining // HOURS_TO_FIX[type]
		
			to_fix = min(remaining_bugs, max_bugs)
		
			week_fix[type] = to_fix
			
			hours_remaining -= to_fix * HOURS_TO_FIX[type]
			bugs_remaining[type] -= to_fix

		fix_list.append(found + [REPAIRERS[week], repairers] + week_fix)
		cumulative = bugs_remaining
	
	print("{},{},{},{},{},{},{},{}".format(*(PRIORITY + HOURS_TO_FIX)))
	
	for row in fix_list:
		print("{},{},{},{},{},{},{},{},{},{}".format(*row))
		