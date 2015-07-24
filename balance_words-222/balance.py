def balance(word):
	def torque(input):
		return sum([ind * (ord(val) - 64) for ind,val in enumerate(input.upper(),start=1)])

	for index, letter in enumerate(word[1:-1:], start=1):
		sub1 = word[:index:]
		sub2 = word[index+1::]
		if torque(sub1[::-1]) == torque(sub2):
			print sub1, letter, sub2, "-", torque(sub2)
			return
	print word, "DOES NOT BALANCE"

# --- inputs ---

balance("STEAD")
balance("CONSUBSTANTIATION")
balance("WRONGHEADED")
balance("UNINTELLIGIBILITY")
balance("SUPERGLUE")
