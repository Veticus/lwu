import argparse


def preflight():
	parser = argparse.ArgumentParser()  # TODO: Create description text

	# Holds the "syntax input"
	# TODO: Create help text
	parser.add_argument("input", nargs="+")

	# The "easy" action args
	# TODO: Create help texts
	parser.add_argument("-v", "--version", action="version", version="%(prog)s")
	parser.add_argument("-h", "-?", "--help", "--?", action="help")

	# The actual functionalities
	# TODO: Create help texts
	parser.add_argument("--add-dict")
	parser.add_argument("-c", "--cleanup", action="store_true")
	parser.add_argument("--import-nogood")
	parser.add_argument("--export-nogood")
	parser.add_argument("--import-wordlist")
	parser.add_argument("--export-wordlist")
	parser.add_argument("-l", "--lang")
	parser.add_argument("-j", "--json", action="store_true")
	parser.add_argument("-a", "--fast-api", action="store_true")





if __name__ == '__main__':
	preflight()
