a, b, c = 1, 2, 3
sum = 2
while True:	
	a = b + c
	if a > 4000000:
		break
	b = a + c
	sum += b
	c = a + b
	if c > 4000000:
		break
print(sum)