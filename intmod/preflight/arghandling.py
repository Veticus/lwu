"""
arghandling

This module is used to deal with taking- and preparing the use of command line arguments for lwu.
It uses the python built-in argparse module, which should keep it rather low-maintenance.
https://docs.python.org/3/library/argparse.html



"""

import argparse
from icecream import ic


def handle_args():
	# TODO: Create description text
	parser = argparse.ArgumentParser()

	# Holds the "syntax input"
	# TODO: Create help text
	parser.add_argument("input", nargs="*")

	# The "easy" action args
	# TODO: Create help texts
	parser.add_argument("-v", "--version", action="version", version="%(prog)s")
	parser.add_argument("-?", "--?", action="help")

	# The actual functionalities
	# TODO: Create help texts
	parser.add_argument("-d", action="store_true", help=argparse.SUPPRESS)  # "Developer mode" flag
	parser.add_argument("--add-dict")
	parser.add_argument("--cleanup", "-c", action="store_true")
	parser.add_argument("--import-nogood")
	parser.add_argument("--export-nogood", nargs='?', const=True)
	parser.add_argument("--import-wordlist")
	parser.add_argument("--export-wordlist", nargs='?', const=True)
	parser.add_argument("--lang", "-l", nargs="?", const="LIST_LANGS")
	parser.add_argument("--json", "-j", action="store_true")
	parser.add_argument("--fast-api", "-a", action="store_true")
	parser.add_argument("--port", nargs="?", const="FASTAPI_PORT_ARG_NO_VALUE_GIVEN", default="FASTAPI_PORT_ARG_NO_VALUE_GIVEN")
	parser.add_argument("--bind-address", nargs="?", const="FASTAPI_BIND_ADDRESS_ARG_NO_VALUE_GIVEN", default="FASTAPI_BIND_ADDRESS_ARG_NO_VALUE_GIVEN")
	parser.add_argument("--config-file")

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
