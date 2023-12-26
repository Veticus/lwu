def find_commonalities(words):
	if not words:
		return {}

	commonalities = {}

	for i in range(len(words)):
		for j in range(i + 1, len(words)):
			common_positions = []

			for pos in range(min(len(words[i]), len(words[j]))):
				if words[i][pos] == words[j][pos]:
					common_positions.append((pos + 1, words[i][pos]))  # Add 1 to convert to 1-based index

			if common_positions:
				key = tuple(sorted([words[i], words[j]]))  # Use a tuple of sorted words as the key
				if key not in commonalities:
					commonalities[key] = common_positions
				else:
					commonalities[key].extend(common_positions)

	return commonalities


words = ["tapir", "patio", "ratio", "cow", "pow"]
result = find_commonalities(words)

if result:
	print("Commonalities between words:")
	for key, value in result.items():
		common_positions_str = ", ".join(f"position {pos}: letter '{letter}'" for pos, letter in value)
		print(f"{key}: {common_positions_str}")
else:
	print("No commonalities found.")
