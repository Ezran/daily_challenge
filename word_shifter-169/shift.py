import re

rows = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
f = open('input','r')

wordlist = {line.strip() for line in open('wordlist.txt')}
shifted = (''.join(row[i:] + row[:i] for row in rows) for i in (-2, -1, 1, 2))
fixes = [str.maketrans(''.join(rows),s) for s in shifted]

for line in f:
	out = [x for x in re.split('[\W]+',line.strip().lower()) if x]
	for word in out:
		if word in wordlist:
			print (word, end=' ')
		else:
			matches = {word.translate(fix) for fix in fixes if word.translate(fix) in wordlist}
			print ('{'+ ', '.join(matches) + '}', end=' ')
	print ('\n')
