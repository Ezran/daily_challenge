import string

trans = str.maketrans('01',' X')

for row in open('input','r'):
	print ('')
	for line in row.split():
		print(str(bin(int(line,16))[2:].zfill(8)).translate(trans))

