import nltk, re, itertools

def makeAdjList():
	adj = {}
	adj[0] = set([1,4,5])
	adj[1] = set([0,2,4,5,6])
	adj[2] = set([1,3,5,6,7])
	adj[3] = set([2,6,7])
	adj[4] = set([0,1,5,8,9])
	adj[5] = set([0,1,2,4,6,8,9,10])
	adj[6] = set([1,2,3,5,7,9,10,11])
	adj[7] = set([2,3,6,10,11])
	adj[8] = set([4,5,9,12,13])
	adj[9] = set([4,5,6,8,10,12,13,14])
	adj[10] = set([5,6,7,9,11,13,14,15])
	adj[11] = set([6,7,10,14,15])
	adj[12] = set([8,9,13])
	adj[13] = set([8,9,10,12,14])
	adj[14] = set([9,10,11,13,15])
	adj[15] = set([10,11,14])
	return adj

def charToDigitsDict(s):
	s = list(s)
	charDict = {}
	index = -1
	for i in s:
		index += 1
		if i not in charDict.keys():
			charDict[i] = [index]
		else:
			charDict[i].append(index)
	return charDict

def getChars(digits,s):
	letters = []
	for i in digits:
		letters.append(s[i])

	return letters

def inPuzzle(word,adj,s):
	charDict = charToDigitsDict(s)
	combinations = wordToDigits(word,adj,charDict)

	for i in combinations:
		if combInPuzzle(i,adj):
			return True

	return False;

def combInPuzzle(comb,adj):

	if len(set(comb)) < len(comb):
		return False

	for i in range(0,len(comb) - 1):
		if comb[i+1] not in adj[comb[i]]:
			return False
	return True

def wordToDigits(w,adj,charDict):
	digits = []
	index = 0
	for i in w:
		if i in charDict.keys():
			digits.append(charDict[i])
			index += 1
		else: 
			return []
	
	output = list(itertools.product(*digits))
	return output

#Capture input
s = raw_input("Enter 16 letters in puzzle top to bottom, left to right: ")
if len(s) != 16:
	print "error"
	quit()

wordlist = [w.lower() for w in nltk.corpus.words.words('en')]
reg = "["+s+"]{,16}"
adj = makeAdjList()
words = [w for w in wordlist if inPuzzle(w,adj,s) and len(w) > 1]
words = list(set(words))
words.sort(key=len)

for w in words:
	print w
