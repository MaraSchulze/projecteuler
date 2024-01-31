numbers = 2000000 * [0]
_sum_ = 0

for number in range(2, 2000000):
	if numbers[number] == 1:
		continue
	_sum_ += number
	i = number
	while i < 2000000:
		numbers[i] = 1
		i += number

print(_sum_)
