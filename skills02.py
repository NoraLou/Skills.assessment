string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string):
	count_unique= {}
	for word in string: 
		count_unique[word] = count_unique.get(word, 0) +1
	return count_unique

print(count_unique(string1))

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""

def common_items(list1, list2):
	# make a dictionary of items in string1
	# if items in string2 appear at least once in string2 then it is a common item. 
	common_items = []
	compare_dict = {}
	for item in list1:
		compare_dict[item] = compare_dict.get(item, 0) +1
	for item in list2:
		if compare_dict.get(item) >= 1:
			common_items.append(item)
	return common_items

print(common_items(list1,list2))


# 1assign + 1assign + (1(for loop) + 1assign  + 1(for loop) + 1compare + 1assign) + 1return

# 3constants + (1n * 1constant) + (1m * 2constant) 

# 3 + 1n + 2n 

# 3 + 3n  = O(n)

"""
Given a list of numbers, return list of number pairs that sum to zero
"""

def sum_zero(list1):
	d = {}
	for item in list1:
		d[item] = d.get(item, -item)
	return [d]

print(sum_zero(list1))

def sum_zero2(list1):
	sum_zero2 = []
	for item in list1:
		item = (item, -item)
		sum_zero2.append(item)
	return sum_zero2

print(sum_zero2(list1))

"""
Given a list of words, return a list of words with duplicates removed
"""

def no_dups(word_list):
	d = {}
	no_dups = []
	for word in word_list:
		d[word] = d.get(word, 0) + 1
	for word in word_list:	
		if d.get(word) > 1:
			no_dups.append(word)
	return no_dups

print(no_dups(words))

# Given a list of words, print the words in ascending order of length
# Bonus: do it on a file instead of the list provided
# Bonus: print the words in alphabetical order in ascending order of length


def word_length(words):
	word_length_lis = []
	for item in words:
		item = (len(item),item)
		word_length_lis.append(item)
	word_length_lis.sort()
	return word_length_lis

print "result",(word_length(words))

"""
# Here's a table of English to Pirate translations
# English     Pirate

# sir         matey
# hotel       fleabag inn
# student     swabbie
# boy         matey
# madam       proud beauty
# professor   foul blaggart
# restaurant  galley
# your        yer
# excuse      arr
# students    swabbies
# are         be
# lawyer      foul blaggart
# the         th'
# restroom    head
# my          me
# hello       avast
# is          be
# man         matey

# Write a program that asks the user to type in a sentence and then
# print the sentece translated to pirate.
# """

 
p_dict = {
	'sir' : 'matey',
	'hotel' :'fleaba inn',
	'student' : 'swabbie',
	'boy' : 'matey',
	'madam' : 'proud beauty',
	'professor' : 'foul blaggart',
	'restaurant' : 'galley',
	'your' : 'yer',
	'excuse' : 'arr',
	'students': 'swabbies',
	'are':'be',
	'lawyer':'foul blaggart',
	'the':'th',
	'restroom':'head',
	'my':'me',
	'hello' : 'avast',
	'is':'be',
	'man': 'matey'
	}

# sentence = raw_input("Please give us a song..")
sentence = "Sir where can I find a hotel for my students ?"

def pirate_translation():
	sentence = "Take the students to the hotel"
	# sentence = raw_input("give me a sentence")
	translation = ""
	split_sentence = sentence.lower().split()
	for i in range(len(split_sentence)):
		if split_sentence[i] in p_dict:
			translation += p_dict.get(split_sentence[i]) + " "
		else: 
			translation += split_sentence[i] + " "
	return translation
	
	

print(pirate_translation()) 















