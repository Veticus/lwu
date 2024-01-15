"""
This module deals with the interactive mode.

- The user can enter a command or lwu syntax in a prompt.
- Commands are evaluated here, and actions taken accordingly.
- Syntax is parsed with intmod.preflight.syntax_parse.py
- Results are shown with print() (or maybe something fancy from the rich package)
- if debug mode is enabled, ic() is used to give extra info. (Maybe look into a decorator for this stuff)
"""
import os
from intmod.preflight.syntax_parse import parse_input_string
from intmod.solver import find_words


flag_exit_asap = False


def interactive_main():
	print("This is interactive mode. Your input, except args, was ignored.")

	while not flag_exit_asap:
		user_input = input("\033[1mLWU >\033[0m")
		parsed_input = parse_input_string(user_input)
		if parsed_input[3]:
			handle_command(parsed_input[3], parsed_input[4])
		else:
			print(f"Parsed input: {parsed_input}")
			print(f"Possible words in wordlist: {find_words(parsed_input[0])}")



def handle_command(command, arg):
	match command:
		case "quit":
			quit()
		case "add":
			print(f"This should add {arg} to the wordlist")
		case "remove":
			print(f"This should remove {arg} from the wordlist")
		case "nogood":
			print(f"This should add {arg} to the nogood list and remove it from the wordlist")
		case "good":
			print(f"This should remove {arg} from the nogood list and add it to the wordlist")
		case "lang":
			print("This should list all languages if no arg is supplied.")
			print("If a valid language is supplied as an arg, the matching list set should be selected.")
			print("If part of a valid language is supplied, all matching languages should be displayed.")
		case "help":
			print("This should show a help text.")
		case "clear":
			if os.name == 'nt':
				_ = os.system('cls')
			else:
				_ = os.system('clear')
		case _:
			print()