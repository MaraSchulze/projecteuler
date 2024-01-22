products = [x * y for x in range(1000) for y in range(1000)]
products.sort()
products = (str(x) for x in products)
palindromes = []
for product in products:
	if product == product[::-1]:
		palindromes.append(product)
print(palindromes[-1])