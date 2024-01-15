from itertools import combinations, permutations

with open('../lists/wordlist.txt', 'r') as f:
	words = f.read().splitlines()



def find_words(letters, words):
	found_words = set()
	for r in range(1, len(letters) + 1):
		for letter_combination in combinations(letters, r):
			for permuted_letters in permutations(letter_combination):
				current_word = ''.join(permuted_letters)
				if current_word in words:
					found_words.add(current_word)
	return list(found_words)


letters = ["s", "t", "e", "a", "k"]
words_found = find_words(letters, words)
print(f"Letters: {letters}")
print(f"Found words: {words_found}")

words_by_length = {}

# group words by
for word in words_found:
	length = len(word)
	if length not in words_by_length:
		words_by_length[length] = []
	words_by_length[length].append(word)

sorted_lists = list(words_by_length.values())

print(f"Words by length: {sorted_lists}")
print(f"Other one: {words_by_length}")


print("\n---\n")

# print lists of found words, in order of words length
for length in sorted(words_by_length.keys()):
	print(f"Words of length {length}:")
	for word in words_by_length[length]:
		print(word)
print()