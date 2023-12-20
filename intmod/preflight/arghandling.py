"""
arghandling

This module is used to deal with taking- and preparing the use of command line arguments for lwu.
It uses the python built-in argparse module, which should keep it rather low-maintenance.
https://docs.python.org/3/library/argparse.html


Usage:
Import from module and call the function as the first thing in the __main__.
For lwu it's done like this:

>>> from intmod.preflight.arghandling import handle_args
>>> if __name__ == '__main__':
>>>     handle_args()

changelog:
2023-12-20:
	- Moved the arg handling stuf in here.
	- Added the hidden "-d" flag to act as a "developer mode".
	- Added dunder meta-variables and module level docstring.
"""

import argparse

from icecream import ic

__version__ = "0.0.1.24"
__date__ = "2023-12-20"
__author__ = "Veticus"
__license__ = "CC BY-NC-SA 4.0"
__all__ = ["handle_args"]


def handle_args():
	"""
	Handle command line arguments.
	Doesn't take any arguments or return anything.

	Should be called as early as possible when the program is called via CLI.
	Argument values will be available as 'args.ARGNAME'.
	For example: 'args.input' holds the input syntax, as given as positional arguments.
	"""
	# TODO: Create description text
	parser = argparse.ArgumentParser(description="")

	# Holds the "syntax input"
	# TODO: Create help text
	parser.add_argument("input",
						nargs="*",
						help="")

	# The "easy" action args
	# TODO: Create help texts
	parser.add_argument("-v", "--version",
						action="version",
						version="%(prog)s",
						help="")

	parser.add_argument("-?", "--?",
						action="help",
						help="")

	# The actual functionalities
	# TODO: Create help texts
	parser.add_argument("-d",
						action="store_true",
						help=argparse.SUPPRESS)  # "Developer mode" flag

	parser.add_argument("--add-dict",
						help="")

	parser.add_argument("--cleanup", "-c",
						action="store_true",
						help="")

	parser.add_argument("--import-nogood",
						help="")

	parser.add_argument("--export-nogood",
						nargs='?',
						const=True,
						help="")

	parser.add_argument("--import-wordlist",
						help="")

	parser.add_argument("--export-wordlist",
						nargs='?',
						const=True,
						help="")

	parser.add_argument("--lang", "-l",
						nargs="?",
						const="LIST_LANGS",
						help="")

	parser.add_argument("--json", "-j",
						action="store_true",
						help="")

	parser.add_argument("--fast-api", "-a",
						action="store_true",
						help="")

	parser.add_argument("--port",
						nargs="?",
						const="FASTAPI_PORT_ARG_NO_VALUE_GIVEN",
						default="FASTAPI_PORT_ARG_NO_VALUE_GIVEN",
						help="")

	parser.add_argument("--bind-address",
						nargs="?",
						const="FASTAPI_BIND_ADDRESS_ARG_NO_VALUE_GIVEN",
						default="FASTAPI_BIND_ADDRESS_ARG_NO_VALUE_GIVEN",
						help="")

	parser.add_argument("--config-file",
						help="")

	args = parser.parse_args()

	# Some icecream to check if it all works as expected, if "developer mode" is used.
	if args.d:
		ic("--- BEGINNING OF ARG HANDLING DEV OUTPUT ---")
		ic(args.d)
		ic(args.input)
		ic(args.add_dict)
		ic(args.cleanup)
		ic(args.import_nogood)
		ic(args.export_nogood)
		ic(args.import_wordlist)
		ic(args.export_wordlist)
		ic(args.lang)
		ic(args.json)
		ic(args.fast_api)
		ic(args.port)
		ic(args.bind_address)
		ic("--- END OF ARG HANDLING DEV OUTPUT ---")
