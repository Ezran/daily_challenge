import csv

array = list()

#Read the input file with csv module
with open('input','r') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ')
	for row in reader:
		array.append(row)
rotate = zip(*array[::-1])
for row in rotate:
	print ' '.join(row)
