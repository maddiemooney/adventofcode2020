def day3(lines, x, y):
	count = 0
	row = 0
	col = 0
	while row < len(lines):
		if(lines[row][col] == '#'):
			count += 1
		row += x
		col = (col + y) % len(lines[0])
	return(count)

file3 = open('input3.txt', 'r')
lines = [line.strip() for line in file3.readlines()]
print(day3(lines, 1, 3))

a = day3(lines, 1, 1)
b = day3(lines, 1, 3)
c = day3(lines, 1, 5)
d = day3(lines, 1, 7)
e = day3(lines, 2, 1)

print(a*b*c*d*e)

