
lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

#print(lines)

for line in lines:
	s = line.split(' ') #每一行都被切割成名叫s的清單
	time = s[0][:5]
	name = s[0][5:]

	print(name)
	#print(s)

