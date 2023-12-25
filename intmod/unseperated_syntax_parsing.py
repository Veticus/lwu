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


# check that all expected combinations get parsed - and that the order doesn't matter
input_length_multi_pospair = "shovel 4 v4 e5"
input_nolength_multi_pospair = "shovel v4 e5"
input_length_single_pospair = "shovel 4 v4"
input_nolength_single_pospair = "shovel e5"
input_length_no_pospair = "shovel 4"
input_nolength_no_pospair = "shovel"
input_length_multi_pospair_out_of_order = "4 v4 shovel"

print("lwu input syntax parsing test")
print("Input format: <letters to use> <length of word> <letter(s) at which position(s)> - not neccessarily in that order")
print("Output format: [identified letters] [identified word length] [identified letter/position pair(s)]")
print()
print(f"Output for input '{input_length_multi_pospair}'\n{parse_input_string(input_length_multi_pospair)}\n")
print(f"Output for input '{input_nolength_multi_pospair}'\n{parse_input_string(input_nolength_multi_pospair)}\n")
print(f"Output for input '{input_length_single_pospair}'\n{parse_input_string(input_length_single_pospair)}\n")
print(f"Output for input '{input_nolength_single_pospair}'\n{parse_input_string(input_nolength_single_pospair)}\n")
print(f"Output for input '{input_length_no_pospair}'\n{parse_input_string(input_length_no_pospair)}\n")
print(f"Output for input '{input_nolength_no_pospair}'\n{parse_input_string(input_nolength_no_pospair)}\n")
print(f"Output for input '{input_length_multi_pospair_out_of_order}'\n{parse_input_string(input_length_multi_pospair_out_of_order)}\n")
