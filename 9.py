
def day9p1(lines):
	preamble = []
	for i in range(25,len(lines)):
		valid = False
		preamble = lines[i-25:i]
		for j in preamble:
			if not valid:
				for k in preamble:
					if j+k == lines[i] and j != k:
						valid = True
						break
		if not valid:
			return(lines[i])

def day9p2(lines):
	target = day9p1(lines)
	for	i in range(0, len(lines)):
		total = 0
		used = [lines[i]]
		while total <= target:
			for j in range(i, len(lines)):
				total += lines[j]
				used.append(lines[j])
				if total == target:
					return(min(used)+ max(used))
				

file9 = open('input9.txt', 'r')
lines = [int(line.strip()) for line in file9.readlines()]
print(day9p1(lines))
print(day9p2(lines))

