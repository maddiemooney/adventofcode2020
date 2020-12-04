# good lord this one is a mess
import re

def day4p1(lines):
	fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	count = 0
	for line in lines:
		valid = True
		
		for f in fields:
			if f not in line:
				valid == False
				break
		if valid:
			count += 1
	return count

def day4p2(lines):
	fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	count = 0
	for line in lines:
		valid = True
		passport = dict()
		for item in line.split():
			field = item.split(':')
			passport[field[0]] = field[1]
		
		for f in fields:
			if f not in passport:
				valid = False
				break
			if f == 'byr':
				if len(passport['byr']) is not 4 or not 1920 <= int(passport['byr']) <= 2002:
					valid = False
					break
			elif f == 'iyr':
				if len(passport['iyr']) is not 4 or not 2010 <= int(passport['iyr']) <= 2020:
					valid = False
					break
			elif f == 'eyr':
				if len(passport['eyr']) is not 4 or not 2020 <= int(passport['eyr']) <= 2030:
					valid = False
					break
			elif f == 'hgt':
				if 'cm' in passport['hgt']:
					if not 150 <= int(passport['hgt'][:-2]) <= 193:
						valid = False
						break
				elif 'in' in passport['hgt']:
					if not 59 <= int(passport['hgt'][:-2]) <= 76:
						valid = False
						break
				else:
					valid = False
					break
			elif f == 'hcl':
				pattern = re.compile("[a-f0-9]+")
				if pattern.fullmatch(passport['hcl'][1:]) is None:
					valid = False
					break
				if passport['hcl'][0] is not '#' or not len(passport['hcl'][1:]) == 6:
					valid = False
					break
			elif f == 'ecl':
				colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
				if not any(c in passport['ecl'] for c in colors):
					valid = False
					break
			elif f == 'pid':
				if len(passport['pid']) != 9:
					valid = False
					break
			
		if valid:
			count += 1
	return(count)

file4 = open('input4.txt', 'r')
toparse = file4.read()
lines = toparse.split("\n\n")
print(day4p1(lines))
print(day4p2(lines))

