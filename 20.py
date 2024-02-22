n = 100
result = 0

f = 1
for i in range(1, n + 1):
	f = f * i

f_string = str(f)
for c in f_string:
	result += int(c)

print(result)
