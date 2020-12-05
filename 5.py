
def day5p1(lines):
	sids = []
	for line in lines:
		rowmin = 0
		rowmax = 127
		colmin = 0
		colmax = 7
		for char in line:
			if char == 'F':
				rowmax = (rowmin+rowmax)//2
			elif char == 'B':
				rowmin = ((rowmin+rowmax)//2) + 1
			elif char == 'L':
				colmax = (colmin+colmax)//2
			elif char == 'R':
				colmin = ((colmin+colmax)//2) + 1
		if rowmin == rowmax and colmin == colmax:
			sid = (rowmin * 8) + colmin
			sids.append(sid)
	
	sids.sort()
	return sids

def day5p2(lines):
	sids1 = []
	sids2 = day5p1(lines)

	for i in range (0,128):
		for j in range (0,8):
			sid = (i*8) + j
			if min(sids2) <= sid <= max(sids2):
				sids1.append(sid)
	
	for sid in sids1:
		if sid not in sids2:
			return sid


file5 = open('input5.txt', 'r')
lines = [line.strip() for line in file5.readlines()]
print(max(day5p1(lines)))
print(day5p2(lines))

