import random
import time
from itertools import permutations

with open('wordlist.txt', 'r') as f:
	words = f.read().splitlines()

print(f"Number of words in file: {len(words)}")
print(f"Random word from words: {random.choice(words)}")


def pospairtest(position, letter, wordlist):
	matchingwords = []
	for word in wordlist:
		if len(word) >= position + 1 and word[position - 1] == letter:
			matchingwords.append(word)
	return matchingwords


# Look for permutations that are found in wordlist
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


start_time = time.time()
validwords = find_words(testletters)
print(f"Words found for the letters {testletters}: {validwords}.\n"
	f"That took {time.time() - start_time:.5f} seconds")


words_matched_to_pospair = pospairtest(testposition, testletter, validwords)
print(f"Of those words, {words_matched_to_pospair} had a '{testletter}' at position {testposition}")
