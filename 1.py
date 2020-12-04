def day1p1(lst):
	for i in lst:
		for j in lst:
			if i+j == 2020:
				return(i*j)

def day1p2(lst):
	for i in lst:
		for j in lst:
			for k in lst:
				if i+j+k == 2020:
					return(i*j*k)

file1 = open('input1.txt', 'r')
lst = [int(line.strip()) for line in file1.readlines()]

print(day1p1(lst))
print(day1p2(lst))

