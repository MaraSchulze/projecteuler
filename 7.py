n = 3
primes = [2]
numbers = set([x for x in range(2, 10**6, 2)])

while len(primes) < 10001:
	if n in numbers:
		n += 2
		continue
	else:
		numbers = numbers.union(set(range(n, 10**6, n)))
		primes.append(n)
	if n > 10**6:
		print("Error")
	n += 2
print(primes, len(primes))
print(max(primes))
