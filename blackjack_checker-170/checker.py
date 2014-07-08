from collections import defaultdict
import re

ranks = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
cards = defaultdict(list)

#######
def getValue(s):
	for i,val in enumerate(ranks):
		if val in s:
			return (i+1 if i < 10 else 10)		
def findWinner():
	numWinners = 0
	nameWinner = ''	
	# check for 5 card wins
	for player in cards:
		if len(cards[player]) > 4:
			numWinners += 1
			nameWinner = player
	if numWinners > 1:
		print "5 card Tie!"
	elif numWinners > 0:
		print nameWinner + " wins with a 5 card hand!"
	else:
		# check for highest hand
		hiHand = 0
		for player in cards:
			l = sum(cards[player])
			if 1 in cards[player]:
				h = l + 10
				if h <= 21:
					if h > hiHand:
						hiHand = h
						numWinners = 1
						nameWinner = player
					elif h == hiHand:
						numWinners += 1
				elif l <= 21:
					if l > hiHand:
						hiHand = l
						numWinners = 1
						nameWinner = player
					elif l == hiHand:
						numWinners += 1
			else:
				if l <= 21:
					if l > hiHand:
						hiHand = l
						numWinners = 1
						nameWinner = player
					elif l == hiHand:
						numWinners += 1
		if numWinners > 1:
			print "It's a tie at " + str(hiHand) + "!"
		elif numWinners > 0:
			print nameWinner + " wins with a " + str(hiHand) + "!"
		else:
			print "No winners!"

#######

for ind in range(1,6):
	cards = defaultdict(list)
	f = open('input'+str(ind),'r')
	for i,row in enumerate(f):
		if i > 0:
			hand = [x for x in re.split('[,:][ ]+',row) if x]
			name = ''
			for j,card in enumerate(hand):
	 			if j == 0:
					name = card
				else:
					cards[name].append(getValue(card))
	print " ==== Test " + str(ind) + " ===="
	findWinner()
