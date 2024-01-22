sum = 0
for current in range(1000):
	if current % 3 == 0 or current % 5 == 0:
		sum += current
print(sum)
