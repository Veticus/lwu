import argparse
from icecream import ic


def preflight():
	# TODO: Create description text
	parser = argparse.ArgumentParser()

	# Holds the "syntax input"
	# TODO: Create help text
	parser.add_argument("input", nargs="*")

	# The "easy" action args
	# TODO: Create help texts
	parser.add_argument("-v", "--version", action="version", version="%(prog)s")
	parser.add_argument( "-?", "--?", action="help")

	# The actual functionalities
	# TODO: Create help texts
	parser.add_argument("--add-dict", metavar="add_dict")
	parser.add_argument("--cleanup", "-c", action="store_true")
	parser.add_argument("--import-nogood", metavar="import_nogood")
	parser.add_argument("--export-nogood", metavar="export_nogood", nargs='?', const=True)
	parser.add_argument("--import-wordlist", metavar="import_wordlist")
	parser.add_argument("--export-wordlist", metavar="export-wordlist", nargs='?', const=True)
	parser.add_argument("--lang", "-l", metavar="lang", nargs="?", const="LIST_LANGS")
	parser.add_argument("--json", "-j", action="store_true")
	parser.add_argument("--fast-api", "-a", action="store_true")
	parser.add_argument("--port", metavar="fastapi_port")
	parser.add_argument("--bind-address", metavar="fastapi_bind_address")
	parser.add_argument("--config-file")

	args = parser.parse_args()

	# Determine if "special modes" are requested
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
	ic(args.fastapi_port)
	ic(args.fastapi_bind_address)









if __name__ == '__main__':
	preflight()
