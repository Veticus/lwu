import re


def parse_input_string(input_string):
	# TODO: Syntax enforcement: Length if length should be range(1, 3)
	# TODO: Syntax enforcement: Only one length int acceptable. If >1 length found, return "syntax error" flag for UI to deal with
	# TODO: Syntax enforcement: If no "letters" supplied, give default or None
	# TODO: Syntax enforcement: Length if letters should be range(1, 26)
	# TODO: Implement "trash" parse: If something that doesn't match 'length', 'positions' or 'letters' found: return "syntax error" flag for UI to deal with

	letters = sorted(
		re.findall(r'[a-zA-Z]', input_string),
		key=lambda x: x.lower()
	)
	lengths = list(map(int, re.findall(r'\b(\d+)\b', input_string)))
	positions = re.findall(r'([a-zA-Z]\d+)', input_string)
	return letters, lengths, positions
