import numpy as np
triangle = []

with open('projecteuler/input_data/p067_triangle.txt', 'r') as file:
	for line in file:
		current_line = line.rstrip('\n').split(' ')
		triangle.append([int(x) for x in current_line])

max_sum = []
previous_line = None
for index,row in enumerate(triangle):
	if not max_sum:
		max_sum.append(row)
	else:
		row_max =np.zeros_like(row)
		for pos, value in enumerate(row):
			row_max[pos] = value + max(max_sum[index-1][max(pos-1,0)],
											max_sum[index-1][min(pos,index-1)])
		max_sum.append(row_max)


print max(max_sum[-1])