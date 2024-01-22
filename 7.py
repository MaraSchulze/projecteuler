n = 3
primes = [2]

while len(primes) < 10001:
	for factor in range(2, int(n**0.5) + 1):
		if n % factor == 0:
			for prime in primes:
				if factor % prime == 0:
					break
			else:
				primes.append(factor)
				print(factor)
	n += 2
print(primes[-1])