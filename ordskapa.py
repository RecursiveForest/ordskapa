# coding=utf8

from random import choice, random
import sys

letters = {'V': ['a', 'å', 'ö', 'i', 'y'], 'C': ['s', 'k', 'ð', 't', 'l', 'r', 'n'], 'S': ['s'], 'R': ['r']}

syllables = {'x': "CVCR"}

patterns = ["CV(CV)(CV)", "(S)CVC(VV(R))", "Vx"]

distributions = {'V': [('ø', .05), ('u', .03)], 'C': [('p', .02)]}
#distributions = {'V': [('ø', 5), ('u', 3)], 'C': [('p', 2)]}
weights = {}
total_dist = 0
for l in distributions:
	weights[l] = []
	for t in distributions[l]:
		total_dist += t[1]
		weights[l].append(t[1])
print(total_dist)
print(weights)

WORDS = 1000

def weighted_choice(weights):
	rnd = random() * sum(weights)
	for i, w in enumerate(weights):
		rnd -= w
		if rnd < 0:
			return i

print(weighted_choice((1 - total_dist, total_dist)))
#sys.exit()

"""for i in range(10):
	print weighted_choice([.7, .3])

exit"""

def skapa(limit, letters, syllables, patterns):
	words = set()

	def frequencies():
		f = {}
		letters = 0
		for word in words:
			for l in word:
				f[l] = f.get(l, 0) + 1
				letters += 1
	
		total = 0
		for l in f:
			total = total + (f[l] / letters)
			print("{} {}: {}".format(total, l, f[l] / letters))

	def generate(pattern):
		word = ''
		i = 0
	
		while i < len(pattern):
			#print("{}: {}".format(i, pattern[i]))
			if pattern[i] == '(':
				if choice([True, False]):
					i += 1
				else:
					for j in range(i, len(pattern)):
						if pattern[j] == ')':
							i = j
							break
			elif pattern[i] == ')':
				i = i + 1
				if not i < len(pattern):
					break
	
			if pattern[i] in letters:
				if weighted_choice((1 - total_dist, total_dist)) and pattern[i] in distributions:
					word = word + distributions[pattern[i]][weighted_choice(weights[pattern[i]])][0]
				else:
					word = word + choice(letters[pattern[i]])
			elif pattern[i] in syllables:
				word = word + generate(syllables[pattern[i]])
			i += 1
	
		return word

	while len(words) < limit:
		words.add(generate(choice(patterns)))

	frequencies()
	
	return words

print(skapa(WORDS, letters, syllables, patterns))
