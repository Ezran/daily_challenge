import string

# vars
trans = str.maketrans('01',' X')

#methods
def rotate(i):
	array = list()
	[array.append(list(row)) for row in i]
	rotate = zip(*array[::-1])
	return [''.join(line) for line in rotate]
	
def zoom_in(i):  #this could be better i think
	ret = list()	
	for line in i:
		newline = list()
		for c in list(line):
			newline.append(c+c)
		for x in range(2):
			ret.append(''.join(newline))
	return ret

def zoom_out(i):
	return [line[::2] for line in i[::2]]

def invert(i): 
	return [line.translate(str.maketrans(' X','X ')) for line in i]	

def pprint(i):
	for line in i:
		print(line)
	print('')

#main
for row in open('input','r'):
	pic = list()
	for line in row.split():
		pic.append(str(bin(int(line,16))[2:].zfill(8)).translate(trans))
	
	pprint(pic)
	for x in range(2):
		pic = zoom_in(pic)
		pprint(pic)
	
	pic = rotate(pic)
	pprint(pic)
	
	pic = invert(pic)
	pprint(pic)
	
	for x in range(2):
		pic = zoom_out(pic)	
		pprint(pic)
