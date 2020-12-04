def day2p1(lines):
	count = 0
	
	for line in lines:
		rule = line.split(':')
		nums = rule[0].split()
		bounds = nums[0].split('-')
		low = bounds[0]
		high = bounds[1]

		pword = nums[1]
		i = 0
		for char in rule[1]:
			if char==pword:
				i += 1
		if int(low) <= i <= int(high):
			count += 1
	
	return(count)
		
def day2p2(lines):
	count = 0
	for line in lines:
		line = line.strip('\n')
		rule = line.split(':')
		nums = rule[0].split()
		bounds = nums[0].split('-')
		low = bounds[0]
		high = bounds[1]

		pword = nums[1]
		a = rule[1][int(low)]==pword
		b = rule[1][int(high)]==pword
		
		if a^b:
			count += 1
		
	return(count)


file2 = open('input2.txt', 'r')
lines = file2.readlines()
print(day2p1(lines))
print(day2p2(lines))

