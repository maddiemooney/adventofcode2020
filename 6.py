# part 2 is awful and really bad code i'm sorry 

def day6p1(lines):
	total = 0
	for line in lines:
			answered = []
			for char in line:
				if char not in answered and char is not '\n':
					answered.append(char)
			total += len(answered)
	return total

def day6p2(lines):
	total = 0
	for line in lines:
		responses = line.split('\n')
		result = [i for i in responses[0]]
		for response in responses:
			for char in response: # why do i need this loop??? idk but it is the incorrect answer without it
				for ans in result:
					if ans not in response:
						result.remove(ans)
		total += len(result)
	return total

	
file6 = open('input6.txt', 'r')
toparse = file6.read()
lines = toparse.split("\n\n")
print(day6p1(lines))
print(day6p2(lines))

