
def day8p1(lines):
	accum = 0
	i = 0
	visited = []
	while(i < len(lines)):
		if i in visited:
			return accum
		else:
			visited.append(i)
			if "nop" in lines[i]:
				i += 1
			elif "acc" in lines[i]:
				accum += int(lines[i].split()[1].strip())
				i += 1
			elif "jmp" in lines[i]:
				i += int(lines[i].split()[1].strip())
			else:
				print("smth is wrong")
	return accum

def test(lines):
	accum = 0
	i = 0
	visited = []
	while(i < len(lines)):
		if i in visited:
			return None
		else:
			visited.append(i)
			if "nop" in lines[i]:
				i += 1
			elif "acc" in lines[i]:
				accum += int(lines[i].split()[1].strip())
				i += 1
			elif "jmp" in lines[i]:
				i += int(lines[i].split()[1].strip())
			else:
				print("smth is wrong")
	return accum


def day8p2(lines):

	for i in range(0, len(lines)):
		temp = lines[:] # this messed me up for a bit :/
		if "nop" in temp[i]:
			temp[i] = temp[i].replace("nop", "jmp")
		elif "jmp" in temp[i]:
			temp[i] = temp[i].replace("jmp", "nop")
		ans = test(temp)
		if ans:
			return ans
		

file8 = open('input8.txt', 'r')
lines = [line.strip() for line in file8.readlines()]
print(day8p1(lines))
print(day8p2(lines))

