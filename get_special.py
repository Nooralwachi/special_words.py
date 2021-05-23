import re
def get_special(filename):
	words=[]
	with open(filename) as f:
		for line in f:
			pattern= r'^((he\w*)|h)er\w*'
			if re.match(pattern, line.strip()):
				words.append(line.strip())
		for word in sorted(words):
			print(word)
get_special('words.txt')