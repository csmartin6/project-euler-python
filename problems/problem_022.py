ascii_offset = 96

with open('projecteuler/input_data/p022_names.txt', 'r') as file:
	line = file.readline()
	names = line.strip().lower().replace("\"","").split(',')

names.sort()
result = 0

for index, name in enumerate(names):
	letter_scores = [(ord(letter)-ascii_offset) for letter in name]
	name_score = sum(letter_scores)
	result += name_score*(index+1)

print result



