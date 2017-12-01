import nltk
from nltk.corpus import cmudict
from nltk.corpus import wordnet as wNet

DictionaryList = ["mon-Key","kou-gar","scape-goat"]

# Load the entire cmudict corpus into a Python dictionary:
transcr = nltk.corpus.cmudict.dict()

#PROGRAM LOGIC




def break_fragment(fragment1):
	#breaks-up fragment in syllables
	print ([transcr[w][0] for w in 'the rabbit ate the hat'.split()])
	phantomObj = ([transcr[w][0] for w in fragment1.split()]) #this translates and converts the input into a list <CAN>
	return phantomObj

def count_syllables(fanta): #receives a tuple
#classifies word in fragment according to the number of syllables
	syllables = 0

	for t in range(0,len(fanta)):
		for i in range(0,len(fanta[t])):
			if fanta[t][i] == '0':
				print fanta[t][i]
				syllables = syllables+1
				if fanta[t][i] == '1':
					print fanta[t][i]
					syllables = syllables+1
				if fanta[t][i] == '2':
					syllables = syllables+1
	return syllables


#Create Empty Slots
LyricLine = [None]*6

def chooseLineType():
	return raw_input("please choose a Line length in syllables: ")

#Choose a blank slot
def chooseSlot ():
	return raw_input("please please choose a slot")

#Add a word to the lyric line
def addWord (slot,word):
	LyricLine[slot] = word
	pass
	

def guessWordA (slotA): #(slot,type)
	for i,v in enumerate (DictionaryList):
		print ("is "+v+" working out for ya?")
		if raw_input().lower().startswith('y') is True:
			LyricLine[slotA] = v
			break
	return v


def guessWordB (slotA): #(slot,type)
	for i,v in enumerate (DictionaryList):
		print ("is "+v+" working out for ya?")
		if raw_input().lower().startswith('y') is True:
			LyricLine[slotA] = v
			break
	return v

def classifyWord (streamWord):
	#Narrow the corpus we are looking at e.g. 'B' will only be in records [5558:5600]
	testTouple = nltk.corpus.cmudict.entries()[653:659]
	#search the tuple for a)number of feet b) 
	tupleTesttuple = testTouple[0]
	name = tupleTesttuple[:1]
	pronounciation = tupleTesttuple[1:]
	print name
	print pronounciation
	for i,v in enumerate(testTouple):
		print testTouple[i]
		#if "u'" in testTouple[i]:
			#print testTouple[i]
		print testTouple.index("(u'acetochlor', [u'AA0', u'S', u'EH1', u'T', u'OW0', u'K', u'L', u'AO2', u'R'])")
	pass

def count_syllablesA(fanta): #receives a tuple
#classifies word in fragment according to the number of syllables
	syllables = 0

	for t in range(0,len(fanta)):
		for i in range(0,len(fanta[t])):
			if fanta[t][i] == '0':
				print fanta[t][i]
				syllables = syllables+1
				if fanta[t][i] == '1':
					print fanta[t][i]
					syllables = syllables+1
				if fanta[t][i] == '2':
					syllables = syllables+1
	return syllables


def pronounce (sentence):
	return ([transcr[w][0] for w in sentence.lower().split()]) 
	
def showLine ():
	print LyricLine
	pass

def readLyric (): #http://www.nltk.org/book/ch00.html #splitting each line into words
	for line in open("/home/candice/Documents/xxx/Music/Lyric Seeds/Walking Away.txt"):
		for word in line.split():
			print(word)
			
#Calling methods hashed out ...		
#readLyric()
#guessWord(5)
#addWord(0,"Take")

print (LyricLine)

