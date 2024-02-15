triangle_number = 1
i = 2
factors = []
d = {}
maxi = 1
while (maxi <= 500):
	triangle_number += i
	i += 1
	factors = [1]
	temp = triangle_number
	factor = 2
	while temp != 1:
		if temp % factor == 0:
			factors.append(factor)
			temp = temp / factor
		else:
			factor += 1
	d[triangle_number] = (len(factors))**2
	maxi = max(maxi, (len(factors))**2)
	print(i - 1, maxi)
