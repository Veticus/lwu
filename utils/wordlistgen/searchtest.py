import re
from itertools import permutations

with open('wordlist.txt', 'r') as f:
	words = f.read().splitlines()


def pospairtest(position, letter, wordlist):
	matchingwords = []
	for word in wordlist:
		if len(word) >= position + 1 and word[position - 1] == letter:
			matchingwords.append(word)
	return matchingwords


# look for permutations that are found in wordlist
def find_words(letters):
	found_words = []
	for permuted_letters in set(permutations(letters)):
		current_word = ''.join(permuted_letters)
		if current_word in words:
			found_words.append(current_word)
	return found_words


testletters = ["s", "h", "o", "v", "e", "l"]
testposition = 4
testletter = "v"

validwords = find_words(testletters)

print(f"Words found for the letters {testletters}: {validwords}")

words_matched_to_pospair = pospairtest(testposition, testletter, validwords)
print(f"Of those words, {words_matched_to_pospair} had a '{testletter}' at position {testposition}")






seperated_input_length_multi_pospair = ["shovel", "4", "v4", "e5"]
seperated_input_nolength_multi_pospair = ["shovel", "v4", "e5"]
seperated_input_length_single_pospair = ["shovel", "4", "v4", ]
seperated_input_nolength_single_pospair = ["shovel", "e5"]
seperated_input_length_no_pospair = ["shovel", "4"]
seperated_input_nolength_no_pospair = ["shovel"]




posletters = [s for s in input if re.compile(r'[a-zA-Z]\d{1,2}').search(s)]
letters = list([s for s in input if re.compile(r'^[a-z]{2,40}$').search(s)])
wordlength = [s for s in input if re.compile(r'^\d{1,2}$').search(s)]

print(posletters)
print(letters)
print(wordlength)
