def find_common_letters(inputwords):
	if not inputwords:
		return []

	min_length = min(len(word) for word in inputwords)  # To get the length of the shortest word, so we don't check beyond the length of the shortest word

	common_letters = []

	for pos in range(min_length):
		letters_at_position = [word[pos] for word in inputwords]
		if all(letter == letters_at_position[0] for letter in letters_at_position):
			common_letters.append((letters_at_position[0], pos + 1))  # Remember to add 1 to convert to 1-based index, for human readability

	return common_letters


words = ["tapir", "patio", "ratio"]
print(f"""Letter/position pairs, that the words {', '.join(f'"{word}"' for word in words[:-1])}{' and ' + f'"{words[-1]}"' if len(words) > 1 else f'"{words[0]}"'} have in common:
{find_common_letters(words)}""")
