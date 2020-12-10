
def day10p1(lines):
	lines.sort()
	start = 0
	current = 0
	jolt1 = 0
	jolt3 = 1
	for i in range(0, len(lines)):
		if lines[i] - current == 1:
			jolt1 += 1
		elif lines[i] - current == 3:
			jolt3 += 1
		current = lines[i]
	return jolt1 * jolt3

# recursion sucks

def day10p2(lines):
	lines.sort()
	paths = {}
	result = getpath(lines, 0, paths)
	return(result)

def getpath(lines, current, paths):

	if current == max(lines):
		return 1

	else:

		# save my poor macbook some processing power
		# this took like 45 mins without this check here :(
		if current in paths:
			return paths[current]
		
		total = 0
		nextpath = [x for x in lines if current < x <= current+3]
		for path in nextpath:
			if path in lines:
				total += getpath(lines, path, paths)	
	
		paths[current] = total
		return total
    

file10 = open('input10.txt', 'r')
lines = [int(line.strip()) for line in file10.readlines()]
print(day10p1(lines))
print(day10p2(lines))

