
result = []
def hasgold(luggages, color):
	if color in luggages:
		for bag in luggages[color]:
			if bag not in result:
				result.append(bag)
			hasgold(luggages, bag)

def countbag(luggages, color):
	total = 0
	if color in luggages:
		for num, bag in luggages[color]:
			total += int(num)
			total += int(num) * countbag(luggages, bag)
	return total

def day7p1(lines):
	luggages = dict()
	for line in lines:
		temp = line.split("contain")
		base = temp[0].split("bags")[0].strip()
		contains = temp[1].split(",")
		for bag in contains:
			bag = bag[2:].split("bag")[0].strip()
			if bag in luggages:
				luggages[bag].append(base)
			else:
				luggages[bag] = [base]
	hasgold(luggages, 'shiny gold')	
	return(len(result))

def day7p2(lines):
	luggages = dict()
	for line in lines:
		temp = line.split("contain")
		base = temp[0].split("bags")[0].strip()
		contains = temp[1].split(',')
		if "no other bags" in contains[0]:
			luggages[base] = []
		else: 
			for bag in contains:
				num = bag[:2].strip()
				bag = bag[2:].split("bag")[0].strip()
				if base in luggages:
					luggages[base].append((num, bag))
				else:
					luggages[base] = [(num, bag)]
	return(countbag(luggages, 'shiny gold'))


file7 = open('input7.txt', 'r')
lines = [line.strip() for line in file7.readlines()]
print(day7p1(lines))
print(day7p2(lines))
