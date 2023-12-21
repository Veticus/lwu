import re

# Ignore allcaps words
# Ignore words with punctuation or numbers
# Ignore single letter words
# Give status ever 1000 words
# No duplicates in letters_file allowed
# All words must be lowercase


with open("inputlist.txt", 'r') as file:
	words = file.read().splitlines()

unique_letters_only = set()

for idx, word in enumerate(words, start=1):
	if (
			re.match("^[a-zA-Z]+$", word)
			and len(word) >= 2
			and not word.isupper()
			and word not in unique_letters_only):
		unique_letters_only.add(word.lower())

	if idx % 1000 == 0:
		print(f"Processed {idx:,} words...")

with open("wordlist.txt", 'w') as file:
	file.write('\n'.join(unique_letters_only))
