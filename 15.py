paths = 21 * [1]

for _ in range(20):
	for i in range(19, -1, -1):
		if (i == 19):
			paths[i] = paths[i] + 1
		else:
			paths[i] = paths[i] + paths[i + 1]

print(paths[0])
