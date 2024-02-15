squares = [x**2 for x in range(998)]

for a in range(1, 996):
	for b in range(a + 1, 997):
		for c in range(b + 1, 998):
			if squares[a] + squares[b] == squares[c] and a + b + c == 1000:
				print(a, b, c, a * b * c)
