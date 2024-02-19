l = []

with open("18_data", "r") as f:
	for line in f.readlines():
		number_list = line.split(" ")
		number_list = [int(number) for number in number_list]
		l.append(number_list)

for row in range(len(l) - 1, 0, -1):
	for column in range(len(l[row]) - 1):
		left = l[row][column]
		right = l[row][column + 1]
		maxi = max(left, right)
		l[row - 1][column] += maxi

print(l[0][0])
