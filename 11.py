grid = []

with open("11_data", "r") as f:
	lines = f.readlines()
for line in lines:
	row = line.split()
	row = [int(s) for s in row]
	grid.append(row)

maxi = 0
for i in range(20):
	for j in range(20):
		if i < 16:
			product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
			maxi = max(maxi, product)
		if j < 16:
			product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
			maxi = max(maxi, product)
		if i < 16 and j < 16:
			product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
			maxi = max(maxi, product)
			product = grid[i+3][j] * grid[i+2][j+1] * grid[i+1][j+2] * grid[i][j+3]
			maxi = max(maxi, product)
			
print(maxi)