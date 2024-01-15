"""
This is where the "magic" happens.

As of now, the wordlist is iterated over, and a match for the input is searched for.
For now this is the most efficient means i have tried.
In the future, i'd like to look into something indexed or other means of solving this faster.
"""

from itertools import permutations

with open('lists/wordlist.txt', 'r') as f:
	words = f.read().splitlines()


def find_words(letters):
	"""
	Iterates through the wordlist, and looks for words that can be spelled using the given letters.
	Input like ['s', 'h', 'o', 'v', 'e', 'l'] should give something like ['shovel', 'shevlo', 'hovels'].

	NOTE: RIGHT NOW THIS ONLY GETS WORDS THAT CAN BE SPELLED WITH ALL GIVEN LETTERS.
	CHECK find_words_with_all_combinations.py FOR A BETTER WAY.


	:param letters: A list of letters, each in a seperate string.
	:return: A list of all words in the wordlist, that can be created using the given letters.
	"""
	found_words = []
	for permuted_letters in set(permutations(letters)):
		current_word = ''.join(permuted_letters)
		if current_word in words:
			found_words.append(current_word)
	return found_words