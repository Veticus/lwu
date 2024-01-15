import re


def parse_input_string(input_string):
	"""
	Parses the lwu input syntax.

	Syntax components:
	1: Letters [required]
	2: Length [optional]
	3: Letter/position pair(s) [optional]
	4: Command [optional]
	5: Command arguments [optional]


	:param input_string:
	:return: letters: A list of the letters of the input string, in alphabetical order.
	:return: position: A list with what is assumed to be the position/letter pairs.
	:return: length: A list with what is assumed to be the length of the desired output.
	:return: command: If an input starts with ":" we assume a command is issued. This is the assumed command. The ":" is stripped.
	:return: arguments: The argument belonging to (following) the command.
	"""
	# TODO: Syntax enforcement: Length if length should be range(1, 3)
	# TODO: Syntax enforcement: Only one length int acceptable. If >1 length found, return "syntax error" flag for UI to deal with
	# TODO: Syntax enforcement: Length if letters should be range(1, 26)
	# TODO: Implement "trash" parse: If something that doesn't match 'length', 'positions' or 'letters' found: return "syntax error" flag for UI to deal with
	# TODO: Implement dev mode

	# Some defaults, to make the rest of the code a little easier on the eyes
	letters = []
	position = []
	length = []
	command = ""
	command_arg = ""

	if input_string.startswith(":"):  # If the input is a command
		command_syntax = re.findall(r':\b[a-z]+\b(?: [a-z]+)?', input_string)[0]

		command = command_syntax.split()[0][1:]
		if len(command_syntax.split()) > 1:
			command_arg = command_syntax.split()[1]

	else:  # If the input is "normal" usage
		letters = re.search(r'\b[a-zA-Z]+\b', input_string)  # Match and ignore the letterpos letter
		letters = letters.group()  # Only get the word
		letters = sorted(letters, key=lambda x: x.lower())  # Sort the letters
		length = list(map(int, re.findall(r'\b(\d+)\b', input_string)))
		position = re.findall(r'([a-zA-Z]\d+)', input_string)

	return letters, length, position, command, command_arg
