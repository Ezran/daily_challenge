import csv

N = 10
array = list()
rot_times = 3
####################################
def rotate(r):
	new_array = list()
	for j in range(N):
		tmp = list()
		for i in reversed(r):
			tmp.append(i[j])
		new_array.append(tmp)
	return new_array

def mprint(r):
	for row in r:
		print ' '.join(row)
	print ""
######################################

#### Main ####
with open('input','r') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ')
	for row in reader:
		array.append(row)
mprint(array)
for i in range(rot_times):
	array = rotate(array)
	mprint(array)

