def sequence(n):
	if n % 2 == 0:
		return n // 2
	else:
		return 3 * n + 1

d = {}
maxi = 0
result = 0
for n in range (1, 10**6):
	length = 0
	current = n
	while current != 1:
		if current not in d:
			current = sequence(current)
			length += 1
		else:
			length += d[current]
			break
	d[n] = length
	if length > maxi:
		maxi = length
		result = n
	print(n, length)
print(maxi, result)
