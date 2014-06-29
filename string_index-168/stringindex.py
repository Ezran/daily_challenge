import sys
import re

inp = "...You...!!!@!3124131212 Hello have this is a --- string Solved !!...? to test @\n\n\n#!#@#@%$**#$@ Congratz this!!!!!!!!!!!!!!!!one ---Problem\n\n"

str_list = [x for x in re.split('[\W]+',inp) if x]
output = list()

for index in sys.argv[1:]:
	if int(index) in range(len(str_list)+1):
		output.append(str_list[int(index)-1])
print ' '.join(output)
