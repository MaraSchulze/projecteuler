n = 600851475143
primes = []

for factor in range(2, int(n**0.5) + 1):
	if n % factor == 0:
		for prime in primes:
			if factor % prime == 0:
				break
		else:
			primes.append(factor)
print(primes)
print(primes[-1])
