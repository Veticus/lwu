import re

from tqdm import tqdm

# Ignore allcaps words
# Ignore words with punctuation or numbers
# Ignore single letter words
# Show some sort of progress indication
# No duplicates in letters_file allowed
# All words must be lowercase


with open("inputlist.txt", 'r') as file:
	words = file.read().splitlines()

unique_letters_only = set()

for idx, word in enumerate(tqdm(words, desc="Processing Words...", unit=" words"), start=1):
	if (
			re.match("^[a-zA-Z]+$", word)
			and len(word) >= 2
			and not word.isupper()
			and word not in unique_letters_only):
		unique_letters_only.add(word.lower())

with tqdm(total=len(unique_letters_only), desc="Writing wordlist file...", unit=" words") as pbar:
	with open("../../lists/wordlist.txt", 'w') as file:
		for word in unique_letters_only:
			file.write(word + '\n')
			pbar.update(1)
