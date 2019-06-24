values = list()
for i in range(0,10):
	values.append(list())
	for j in range(0,10):
		values[i].append(0)
		
value = 1
srow = 0
scol = 0
erow = 9
ecol = 9

for i in  range(0,5) :
	
	for j in range(scol,ecol + 1) :
		values[srow][j] = value
		value += 1
	
	srow += 1
	
	for j in range( srow , erow + 1 ) :
		values[j][ecol] = value
		value += 1
		
	ecol -= 1
	
	for j in range( ecol , scol - 1, -1 ) :
		values[erow][j] = value
		value += 1
		
	erow -= 1
	
	for j in range( erow , srow - 1, -1 ):
		values[j][scol] = value
		value += 1
		
	scol += 1
		
for i in range(0,10):
	for j in range(0,10):
		print( values[i][j] , end=' ')
		if values[i][j] < 10 :
			print("  ",end='')
		elif values[i][j] < 100 :
			print(" ",end='')
	print()